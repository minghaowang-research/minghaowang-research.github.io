#!/usr/bin/env python3
"""Build, preview, and audit this site (see README.md).

  python3 _tools/site.py install   one-time: bundler + gems on Homebrew ruby@3.3
  python3 _tools/site.py build     jekyll build -> _site/
  python3 _tools/site.py serve     live preview at http://localhost:4000
  python3 _tools/site.py audit     build + internal link check + consistency checks
                                   + screenshots of every page (1280 and 500 px) in _audit/
"""
import functools, html, http.server, os, pathlib, re, shutil, subprocess, sys, threading

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "_site"
AUDIT = ROOT / "_audit"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
SITE_URL = "https://minghaowang-research.github.io"
SHOT_HEIGHT = 4500                     # headless Chrome captures the window, not the full page
GEM_HOME = str(pathlib.Path.home() / ".gem" / "jekyll-site")
ENV = dict(os.environ, GEM_HOME=GEM_HOME, BUNDLE_PATH=GEM_HOME,
           PATH="/opt/homebrew/opt/ruby@3.3/bin:" + GEM_HOME + "/bin:" + os.environ["PATH"])
CFG = ["--config", "_config.yml,_config_docker.yml"]   # second file blanks `url` so links are relative


def need_bundle():
    if not shutil.which("bundle", path=ENV["PATH"]):
        sys.exit("bundle not found. Install Homebrew ruby@3.3 (brew install ruby@3.3), then: python3 _tools/site.py install. "
                 "Intel Mac: edit the /opt/homebrew path at the top of this script to /usr/local.")


def install():
    if not shutil.which("gem", path=ENV["PATH"]):
        sys.exit("Ruby not found at /opt/homebrew/opt/ruby@3.3. Run: brew install ruby@3.3")
    subprocess.run(["gem", "install", "bundler", "--no-document"], cwd=ROOT, env=ENV, check=True)
    subprocess.run(["bundle", "install"], cwd=ROOT, env=ENV, check=True)


def build():
    need_bundle()
    r = subprocess.run(["bundle", "exec", "jekyll", "build"] + CFG, cwd=ROOT, env=ENV,
                       capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    bad = [l for l in out.splitlines() if re.search(r"error|warning|Liquid", l, re.I) and "faraday-retry" not in l]
    print(out.splitlines()[-1] if out else "")
    if r.returncode or bad:
        print("BUILD PROBLEMS:\n  " + "\n  ".join(bad or [out[-800:]]))
    return r.returncode == 0 and not bad


def serve():
    need_bundle()
    os.chdir(ROOT)
    os.execvpe("bundle", ["bundle", "exec", "jekyll", "serve", "-l", "-H", "localhost"] + CFG, ENV)


def pages():
    out = []
    for p in sorted(SITE.rglob("*.html")):
        if 'http-equiv="refresh"' in p.read_text(errors="ignore"):
            continue                                   # redirect stubs from jekyll-redirect-from
        out.append(p)
    return out


def resolve(href, page):
    href = html.unescape(href).split("#")[0].split("?")[0]
    for own in (SITE_URL, "http://localhost:4000"):      # links to our own domain are internal
        if href.startswith(own):
            href = href[len(own):] or "/"
    if not href or href.startswith(("http://", "https://", "mailto:", "tel:", "//", "data:")):
        return None
    p = SITE / href.lstrip("/") if href.startswith("/") else page.parent / href
    candidates = [p, p / "index.html", p.with_suffix(".html")]   # extensionless permalinks work on GitHub Pages
    return any(exists_exact(c) for c in candidates)


def exists_exact(p):
    """is_file() is case-insensitive on APFS; GitHub Pages is case-sensitive."""
    try:
        return p.is_file() and p.name in os.listdir(p.parent)
    except OSError:
        return False


def check_links():
    missing = []
    for page in pages():
        txt = page.read_text(errors="ignore")
        for m in re.finditer(r'(?:href|src)="([^"]+)"', txt):
            if resolve(m.group(1), page) is False:
                missing.append((page.relative_to(SITE).as_posix(), m.group(1)))
    return missing


def check_consistency():
    problems = []
    nav = re.findall(r"url:\s*(\S+)", (ROOT / "_data" / "navigation.yml").read_text())
    for u in nav:
        if not (SITE / u.strip("/") / "index.html").is_file():
            problems.append(f"navigation.yml url {u} has no built page")
    seo_nav = re.findall(r'"url": "\{\{ seo_url \}\}(/[^"]+)"', (ROOT / "_includes" / "seo.html").read_text())
    if sorted(seo_nav) != sorted(nav):
        problems.append(f"seo.html SiteNavigationElement list {seo_nav} differs from navigation.yml {nav}")
    for name in ("files/Minghao-Wang-PhD-CV.pdf", "images/profile.png", "assets/css/site.css"):
        if not (ROOT / name).is_file():
            problems.append(f"missing {name}")
    for m in re.finditer(r'url:\s*"?([^"\s}]*)', (ROOT / "_data" / "papers.yml").read_text()):
        if not m.group(1):
            problems.append("papers.yml has a link with an empty url")
    for p in sorted(ROOT.glob("_pages/*.md")):
        if p.name != "404.md" and "description:" not in p.read_text().split("---")[1]:
            problems.append(f"{p.name}: no description in front matter (SEO)")
    for page in pages():
        t = page.read_text(errors="ignore")
        if re.search(r"\{%|\{\{ ", t):
            problems.append(f"{page.relative_to(SITE)}: raw Liquid in output")
        if re.search(r"(?m)^\s*#{1,3} \S", re.sub(r"<pre.*?</pre>", "", t, flags=re.S)):
            problems.append(f"{page.relative_to(SITE)}: raw markdown heading in output")
    # teaching.md shows years in parentheses; each course page must have a matching '## YYYY' section
    teaching = (ROOT / "_pages" / "teaching.md").read_text()
    # matches "(2025, 2026)" and "(Fall 2026)" but not "(Updated September 2025)"
    for years, slug in re.findall(r"\(((?:(?:Spring|Summer|Fall|Winter) )?\d{4}(?:, (?:(?:Spring|Summer|Fall|Winter) )?\d{4})*)\)\]\(\{\{ base_path \}\}/teaching/([\w-]+)\)", teaching):
        body = (ROOT / "_teaching" / f"{slug}.md").read_text() if (ROOT / "_teaching" / f"{slug}.md").is_file() else ""
        for y in re.findall(r"\d{4}", years):
            if f"## {y}" not in body:
                problems.append(f"teaching.md lists {y} for {slug} but _teaching/{slug}.md has no '## {y}' section")
    return problems


class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass


def screenshots():
    if not os.path.exists(CHROME):
        return None
    AUDIT.mkdir(exist_ok=True)
    for f in AUDIT.glob("*.png"):
        f.unlink()
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quiet, directory=str(SITE)))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    port = srv.server_address[1]
    shots = []
    for page in pages():
        rel = page.relative_to(SITE).as_posix()
        name = rel.replace("/index.html", "").replace("index.html", "home").replace(".html", "").replace("/", "_")
        for w in (1280, 500):                          # headless Chrome will not go narrower than 500 px
            out = AUDIT / f"{name}_{w}.png"
            subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                            "--virtual-time-budget=6000", f"--window-size={w},{SHOT_HEIGHT}",
                            f"--screenshot={out}", f"http://127.0.0.1:{port}/{rel}"], capture_output=True)
            if out.is_file():
                shots.append(out)
    srv.shutdown()
    return shots


def audit():
    ok = build()
    missing, problems = check_links(), check_consistency()
    shots = screenshots()
    if shots is None:
        problems.append("Google Chrome not found, no screenshots taken; install Chrome or look at the site in a browser")
        shots = []
    print(f"\nPages: {len(pages())}   Broken internal links: {len(missing)}   "
          f"Consistency problems: {len(problems)}   Screenshots: {len(shots)} in {AUDIT.name}/")
    for p, h in missing:
        print(f"  BROKEN   {p} -> {h}")
    for p in problems:
        print(f"  PROBLEM  {p}")
    print("\nNext: open every screenshot in _audit/ and look at it (clipping, overlap, empty sections, "
          "raw markdown, nav highlight, hero, paper cards) before reporting.")
    sys.exit(0 if ok and not missing and not problems else 1)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "audit"
    {"install": install, "build": build, "serve": serve, "audit": audit}.get(cmd, lambda: print(__doc__))()

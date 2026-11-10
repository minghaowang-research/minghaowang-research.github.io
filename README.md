# minghaowang-research.github.io

Personal academic website of Minghao Wang (PhD student in Marketing, Michigan State University).
Jekyll on GitHub Pages, custom single-column design (since 2026-11-02). This file is the operating
manual for whoever maintains the site next, human or AI agent (Claude, Codex, Copilot, anyone). Read it before
changing anything. `AGENTS.md` is the short version that coding agents pick up automatically; this file is the full one.

## 0. Quick start for a new agent or a new machine

1. Clone the repo: `git clone https://github.com/minghaowang-research/minghaowang-research.github.io.git`.
2. Read this README (sections 1, 2, 4, 6 at least) and `AGENTS.md`.
3. If you will build locally: `brew install ruby@3.3` then `python3 _tools/site.py install` (section 5). Not required for text edits.
4. Local trackers (`_CHANGELOG.md`, `_FOLDER_MAP.md`, `CLAUDE.md`) are gitignored and will not be in a fresh clone. Create
   `_CHANGELOG.md` with the table header below and log from there; `git log` holds the older history.
   ```
   | Date | File | Action | Archive name | Note |
   |---|---|---|---|---|
   ```
5. Three rules that never bend: push only when the owner says so; archive before replacing or deleting; run `check` or `audit` before every push.

## 1. How the site is maintained

The loop is always the same:

1. Edit content or design in this folder (the local git clone). Section 2 says which file.
2. Text-only edit (a paper, a date, a bullet): `python3 _tools/site.py check` (build, links, consistency; no screenshots).
   Layout change or many pages: `python3 _tools/site.py audit` (the same plus screenshots of every page into `_audit/`), then look at the screenshots.
3. Fix what is wrong. Repeat.
4. Commit on `master` and push, after the owner's OK. GitHub Pages rebuilds within a minute or two.
5. Look at the live page once (`https://minghaowang-research.github.io/` or the page you changed).

The owner works online: no local preview unless they ask for one (`python3 _tools/site.py serve`).

GitHub is the backup: every push is a full off-machine copy. Before any large change, tag the current
state (`git tag pre-<change>-<date>`), work on a branch, and snapshot the files you will replace into `_Archive/` (see section 8).

Never push without the site owner's OK. Never delete a file without archiving it first.

## 2. Where everything lives

| What you want to change | Edit this | Notes |
|---|---|---|
| Biography, research interests | `_pages/about.md` | Homepage body. Markdown only. `## Heading` becomes a section heading. The "Recent Work" section is `{% include recent.html %}` (first 3 entries of `papers.yml`). |
| Education, awards, certifications (homepage rows) | `_data/cv.yml` | Three lists (`education`, `awards`, `certifications`), rendered by `_includes/cv.html` from `about.md`. See section 4. |
| Name, tagline, hero links (email, MSU profile, LinkedIn, GitHub) | `_config.yml` under `author:` | The hero reads these fields; a blank field hides its link. The tagline is two lines: `bio` (role) and `affiliation`. CV button is fixed to `files/Minghao-Wang-PhD-CV.pdf`. Google Scholar button appears as soon as `googlescholar:` in `_config.yml` has a URL (blank today). ORCID button sits in `_includes/hero.html` inside a Liquid comment, switched off by the owner's choice (the ORCID in `_config.yml` still feeds the JSON-LD). Chinese name is hardcoded there too. |
| Greeting words (small green line above the name on the homepage, cycles every 2.4 s, 30 languages) | `_layouts/default.html`, the `words` list in the script at the bottom; the element is in `_includes/hero.html` | Owner's order: Hello, 你好, Hola, 안녕하세요, こんにちは, Bonjour, then the rest. Keep "Hello" first. |
| Working papers (list with status and, when present, link buttons) | `_data/papers.yml` | One entry per paper. See section 4. |
| Conference presentations, symposia, professional service | `_pages/research.md` | Markdown bullets. Working papers are NOT here; the page includes the list from `papers.yml`. |
| Teaching overview page | `_pages/teaching.md` | Links to course pages with years in parentheses. |
| A course or teaching document | `_teaching/<slug>.md` | One page per course across all years (`## 2026`, `## 2025` sections). Front matter in section 4. |
| Tools and software | `_pages/tools.md` | Markdown. `[text](url){: .btn}` makes a pill button. |
| Photography and travel | `_pages/travel.md` | Update the counts in the intro paragraph when lists change. |
| Top navigation | `_data/navigation.yml` and the `SiteNavigationElement` list in `_includes/seo.html` | Both must match; the audit checks this. Labels: Research, Teaching, Software (URL stays /tools/), Travel. |
| CV PDF, syllabi, other downloads | `files/` | Keep file names stable; links point at them. |
| Profile photo, favicons | `images/` | `profile.png` is the hero photo (`author.avatar` in `_config.yml`). |
| Web appendix for a paper | `appendix/<project>/` | Create on first use. URL `/appendix/<project>/<file>`. |
| Colors, fonts, spacing, components | `assets/css/site.css` | The only stylesheet. Section 3. |
| Page skeleton: nav, hero slot, footer, fonts | `_layouts/default.html` | Loads `site.css`, `_includes/seo.html`, `_includes/head/custom.html` (favicons, MathJax), `_includes/analytics.html`. |
| Page body layouts | `_layouts/archive.html` (pages), `_layouts/single.html` (teaching pages, adds the type and venue line) | Both render `page-title` + `.content`. |
| Hero, paper list, recent list, CV rows, footer | `_includes/hero.html`, `_includes/papers.html`, `_includes/recent.html`, `_includes/cv.html`, `_includes/footer.html` | Footer is the copyright line only (owner wants it clean). `sitemap.xml` is generated by jekyll-sitemap and referenced from robots.txt. |
| SEO meta, JSON-LD, Search Console tag | `_includes/seo.html`, `google_site_verification` in `_config.yml` | Never clear the verification value. |
| Analytics | `_config.yml` `analytics:` (GA4) | |
| Audit and build tool | `_tools/site.py` | Section 5. |
| Trackers (local only, gitignored) | `CLAUDE.md`, `_CHANGELOG.md`, `_FOLDER_MAP.md` | Update after every change. Absent in a fresh clone; see section 0. |
| Agent instructions (committed) | `README.md` (this file), `AGENTS.md` (short version read automatically by Codex, Cursor, Copilot and similar) | Keep both in step. Claude Code reaches this README through the owner's `update-website` skill. |
| Snapshots | `_Archive/` | Read-only history. `theme_2026-11-02_v1/` holds the old Academic Pages theme. |

The Academic Pages theme leftovers (`_sass/`, theme includes and layouts, `assets/js`, fonts, Docker and npm files) were
removed on 2026-11-02. What a page needs is now exactly what is in `_layouts/` (4 files), `_includes/` (hero, papers, recent, cv,
footer, seo, analytics, head/custom, base_path) and `assets/css/site.css`. The old files are in the git tag
`pre-redesign-2026-11-02` and, for the text files, in `_Archive/theme_2026-11-02_v1/`. `_config.yml` still carries unused
theme settings (comments, staticman, publications/talks/portfolio collections); they are inert and were left alone.

## 3. Design system

One stylesheet, `assets/css/site.css`, plain CSS, no build step. Everything hangs off the variables at the top.

| Token | Value | Used for |
|---|---|---|
| `--accent` | `#18453B` (MSU Spartan green, 10.2:1 on ivory) | active nav item, text links, the CV button, the bar above section headings, the status tag, the homepage greeting (since 2026-11-09). `--accent-soft` and `--accent-line` are the same green at low opacity; change all three to move to another school's color. |
| `--bg` / `--surface` | `#faf9f6` / `#ffffff` | ivory page background / white cards and pills |
| `--text` / `--muted` / `--faint` | `#1f1f1d` / `#5f5f58` / `#73736b` | body / secondary text / footer. Contrast on ivory: 15.7:1, 6.1:1, 4.5:1 (all WCAG AA) |
| `--font-body` | Inter (Google Fonts) | everything |
| `--font-serif` | Source Serif 4 (Google Fonts) | name in the hero, page titles, section headings, paper titles, nav brand |

Layout: one centered column, max width 800 px, sticky top nav with small uppercase links (the current page is underlined in green). No sidebar.

Components and how markdown maps to them:

- `# Page title` comes from front matter `title:` and renders as `.page-title` (serif, 34 px). The homepage shows the hero instead.
- `## Heading` in content renders as a serif section heading (25 px) with a short green bar above it. A `---` right before a `##` is hidden by the stylesheet (the bar already separates sections). `# Heading` inside content is a serif subtitle (28 px); the page title comes from front matter.
- `### Heading` is a normal bold subheading (17 px).
- `[text](url){: .btn}` is a pill button. Paper link buttons use the same class.
- `<details markdown="1"><summary>...</summary>` renders as a collapsible card (used on the CCT page).
- Working papers (`.pub`) are generated from `_data/papers.yml` by `_includes/papers.html`: serif title (h3), authors with the owner's name in bold, status as a small green tag, and pill buttons only when `links` has entries. No box: the owner decided an empty card draws the eye for nothing; buttons appear by themselves once SSRN or DOI links exist. `_includes/recent.html` shows the first three the same way on the homepage (same sizes: title 20 px, authors 15 px).
- CV rows (`.cv`) are generated from `_data/cv.yml` by `_includes/cv.html`: title, place in grey below, date right-aligned. Used for Education, Awards and Certifications on the homepage.
- Hero: cycling greeting, name + Chinese name, two-line tagline (`author.bio`, `author.affiliation`), a solid green CV button followed by plain text links (Email, MSU Profile, LinkedIn, GitHub), portrait photo with rounded corners (150 x 180 px).
- Nav brand: the site name (`name:` in `_config.yml`), links home. The greeting above the name on the homepage cycles through languages for three passes, then rests; off for visitors who prefer reduced motion. The only script besides Google Analytics; MathJax loads only on pages with `mathjax: true` in front matter.
- Inline scripts: no `//` line comments. The `compress` layout joins all lines in production, so a `//` comment would swallow the rest of the script. Use `/* */`.

Rules: no new colors outside the variables, no inline styles in markdown, no new fonts, no more JavaScript unless a feature truly needs it. Mobile breakpoint is 640 px.

## 4. Content formats

Working paper (`_data/papers.yml`):

```yaml
- title: "Paper Title"
  authors: "**Minghao Wang**, Coauthor One, and Coauthor Two"   # natural order for everyone; bold the owner
  year: 2026
  status: "Under review"      # Working paper | Under review | R&R | Forthcoming (no journal names: owner's choice for now)
  # abstract: "One paragraph."  # optional; shown behind an "Abstract" toggle when present
  links: []                   # or: [{ label: "SSRN", url: "https://ssrn.com/abstract=..." }, { label: "PDF", url: "/files/x.pdf" }]
```

Homepage row (`_data/cv.yml`, under `education:`, `awards:` or `certifications:`, newest first):

```yaml
  - { title: "Master of Science (M.S.) in Marketing Research", place: "Michigan State University", date: "2020" }
```

Conference presentation (`_pages/research.md`):

```
- **Minghao Wang**, Coauthor, and Coauthor (YYYY), "Title", Type, *Conference Name*, City, Country
```

Course page (`_teaching/<slug>.md`), one page per course for all years:

```yaml
---
title: "MKT 327: Introduction to Marketing"
collection: teaching
type: "Undergraduate course"
permalink: /teaching/marketing-327
venue: "Michigan State University, East Lansing, MI"
date: YYYY-MM-DD
categories: [teaching-experience]
excerpt: " "
---
<!-- excerpt-end -->

## 2026
**Summer Session:** June 30 - August 14, 2026
**Students:** 87
**Student Rating:** 4.30/5
```

On `_pages/teaching.md` the link shows the years: `**[MKT 327: Introduction to Marketing (2025, 2026)]({{ base_path }}/teaching/marketing-327)**`.
The audit checks that each year in parentheses has a `## YYYY` section on the course page.

Standalone teaching document (philosophy, policy): `layout: archive`, `permalink: /teaching/<slug>`, `categories: [<category>]`, `author_profile: true`.

Author names are in natural order everywhere on the site (First Last, with "and" before the last author); the inverted "Wang, Minghao" form stays in the CV. Owner's name in author lists is always bold. The biography is in first person (owner's choice 2026-11-02, after a survey of 10 marketing sites: all first person, none with inline school logos, so no logos here). Research identity: marketing strategy, digital marketing, public policy, customer satisfaction, causal inference.

## 5. Local build, preview, audit

Requirements (macOS): Homebrew `ruby@3.3` (Ruby 4 cannot compile Jekyll 3.10's native gems on Apple clang 16), Google Chrome for screenshots.
Gems install to `~/.gem/jekyll-site`, outside the repo.

```
brew install ruby@3.3
python3 _tools/site.py install     # once per machine
python3 _tools/site.py build       # -> _site/
python3 _tools/site.py serve       # http://localhost:4000, live reload
python3 _tools/site.py check       # build + link and consistency checks, no screenshots (text-only edits)
python3 _tools/site.py audit       # the same plus screenshots in _audit/ (gitignored); after any layout change
```

The audit exits 1 if the build logs a warning, an internal link is broken, or a consistency check fails. It also prints the
screenshot list; the agent must open and look at them. Headless Chrome cannot render narrower than 500 px, so the mobile
check uses 500 px. Screenshots capture a 4500 px tall window, not the full page; very long pages are cut at the bottom.

## 6. Audit checklist

Run this before every push and whenever asked to "check" or "audit" the website.

1. `python3 _tools/site.py audit` passes (no BROKEN, no PROBLEM, no build warnings). For a text-only edit (a paper, a date, a bullet) `check` is enough: same checks, no screenshots; look at the live page after the push instead.
2. After layout changes, look at every screenshot in `_audit/` at both widths: nothing clipped or overlapping, hero intact, nav highlights the current page, section headings in order, paper cards render, no raw markdown or Liquid, footer present.
3. Content cross-checks the script cannot do:
   - `_pages/about.md` and `_data/cv.yml` match the current CV PDF (degrees, awards, certifications, expected graduation year). Do not write a year count ("second-year"); it goes stale every August. Say "since Fall 2024".
   - Every working paper in `papers.yml` that has a conference presentation appears in `research.md` with the same title.
   - Counts in `_pages/travel.md` intro match the lists.
   - Years in `teaching.md` parentheses match the course pages (script checks this too).
   - `_config.yml` `author:` fields are current (email, LinkedIn, ORCID, MSU profile).
4. Live site after push: fetch `https://minghaowang-research.github.io/` and one subpage, confirm the new content is there and `site.css` loads (view source).
5. Record what was audited and fixed in `_CHANGELOG.md`.

## 7. Deploy

- Branch: `master` is the live branch. GitHub Pages builds automatically (Jekyll 3.10 with the `github-pages` gem). No Actions workflow.
- Large changes (design, structure) go on a branch and are merged into `master` (fast-forward) once the owner approves the result; the branch is then deleted. The 2026-11-02 redesign was done this way.
- `git add -A && git commit -m "<what changed>" && git push origin master`, only after the owner says push.
- Verify: `gh api repos/minghaowang-research/minghaowang-research.github.io/pages/builds/latest --jq .status` should be `built`.

## 8. Archive and recovery

- Before replacing or deleting a file: copy it to `_Archive/<source-folder>/<name>_<YYYY-MM-DD>_v<N>.<ext>` and log it.
- The pre-redesign site is tagged `pre-redesign-2026-11-02` in git and copied to `_Archive/theme_2026-11-02_v1/`
  (layouts, includes, sass, main.scss, config, navigation, research page). To go back: `git checkout pre-redesign-2026-11-02`.

## 9. Decisions

| Date | Decision | Why |
|---|---|---|
| 2026-11-02 | Replaced the Academic Pages / Minimal Mistakes theme with one hand-written stylesheet and three small layouts; markdown content untouched | The stock theme looked generic and fought every styling change. An agent can now restyle anything by editing one file. Inspired by a colleague's single-page site built with an agent in the loop. |
| 2026-11-02 | Working papers moved from markdown bullets to `_data/papers.yml`, rendered as a plain list (boxes tried and dropped the same day) | Link buttons need structure; YAML keeps it editable without HTML. Boxes without buttons looked empty; the list grows buttons on its own when links are added. Other research lists stay markdown. |
| 2026-11-02 | Accent color is a single CSS variable, set to MSU green | Owner may move schools; the color changes in one line. |
| 2026-11-02 | Repo stays in `~/Documents/Visual Studio Code/` (iCloud-synced Documents) | Moving it gains nothing: Documents is already iCloud; GitHub is the real backup. |
| 2026-11-02 | Local build on Homebrew ruby@3.3, gems outside the repo | Ruby 4 fails to compile `json`/`racc`/`http_parser.rb` on Apple clang 16. GitHub Pages also runs Ruby 3.3. |
| 2026-11-02 | Nav brand is a cycling greeting instead of the name; hero shows Email, MSU Profile, LinkedIn, GitHub, CV | Owner liked the greeting on the colleague's site. Google Scholar and ORCID buttons stay in the template, switched off by the owner's choice. |
| 2026-11-02 | Green used sparingly: active nav, hover only; tags outlined; links charcoal | Owner asked for a high-end feel; luxury palettes are near-monochrome with the accent in small doses. |
| 2026-11-02 | Footer is one copyright line; sitemap generated by jekyll-sitemap (static file removed) | Owner wants it clean; the old static sitemap was stale (8 URLs, May 2026). |
| 2026-11-02 | Author names in natural order on the site (First Last, "and" before the last); inverted form only in the CV | Reads as prose, not as a reference list; consistent for every paper regardless of who is first author. |
| 2026-11-02 | `check` (no screenshots) for text-only edits, `audit` for layout changes; no local preview by default | Owner works online and did not want Chrome windows for every small edit. The screenshot pass stays for anything that can break layout. |
| 2026-11-02 | Theme leftovers deleted from the tree rather than copied into `_Archive/` | Already archived twice (git tag + theme snapshot); copying 2.5 MB of third-party fonts and JS into the public archive folder would only bloat the repo. Small text files were added to the snapshot before deletion. |
| 2026-11-09 | Design pass "C": serif section headings with a green bar, green text links and status tag, solid green CV button with plain text links, portrait photo, CV rows from `_data/cv.yml`, column 800 px, name in the nav and the greeting above the name on the homepage | Owner asked again for a more high-end look and picked this version from six rendered previews (label-left layout rejected: the labels took too much space). Replaces the 2026-11-02 "green used sparingly" and "nav brand is a greeting" rows. Footer stays one line. |
| 2026-11-02 | Audit = script checks + screenshots that the agent must look at | Build logs and link checks miss layout breakage; the screenshot step is what caught the clipped mobile view and the old theme's wasted sidebar. |

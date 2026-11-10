# Instructions for coding agents

Personal academic website of Minghao Wang, Jekyll on GitHub Pages. `README.md` is the full manual; read it before
editing anything. This file is the short version.

## Rules

- Never push without the owner's explicit OK. Commit freely; pushing publishes.
- Never delete or replace a file without first copying it to `_Archive/<folder>/<name>_<YYYY-MM-DD>_v<N>.<ext>`.
- Before every push run `python3 _tools/site.py check` (text-only edits) or `python3 _tools/site.py audit`
  (layout changes; then open and look at the screenshots in `_audit/`). Fix anything it reports.
- Content is markdown. Design lives in one file, `assets/css/site.css`; `--accent` is the only color to change for a
  new school. No new colors, fonts, inline styles, or scripts. No `//` comments inside inline scripts (production
  build joins lines).
- Author names in natural order ("Minghao Wang, Hang Nguyen, and ..."), the owner's name in bold. No year counts
  like "second-year" in the biography; say "since Fall 2024".
- Keep `_data/navigation.yml` and the `SiteNavigationElement` list in `_includes/seo.html` in step. Never clear
  `google_site_verification` in `_config.yml`.

## Where things live

| Change | File |
|---|---|
| Biography, education, awards | `_pages/about.md` |
| Working papers (status, links) | `_data/papers.yml` |
| Conferences, service | `_pages/research.md` |
| Teaching index / a course page | `_pages/teaching.md` / `_teaching/<slug>.md` |
| Tools, travel | `_pages/tools.md`, `_pages/travel.md` |
| Hero name, tagline, links | `_config.yml` under `author:` (buttons in `_includes/hero.html`) |
| Education, awards, certifications on the homepage | `_data/cv.yml` |
| Greeting words in the nav | `_layouts/default.html`, bottom script |
| CV PDF and downloads | `files/` |
| Look and feel | `assets/css/site.css`, layouts in `_layouts/`, includes in `_includes/` |

## Commands

```
python3 _tools/site.py check    # build + link and consistency checks
python3 _tools/site.py audit    # the same + screenshots of every page into _audit/
python3 _tools/site.py serve    # local preview at http://localhost:4000 (only if the owner asks)
python3 _tools/site.py install  # once per machine, after: brew install ruby@3.3
```

Deploy: `git push origin master` after the owner's OK; GitHub Pages builds in about a minute. Verify with
`gh api repos/minghaowang-research/minghaowang-research.github.io/pages/builds/latest --jq .status`.

Recovery: the pre-redesign site is git tag `pre-redesign-2026-11-02` and `_Archive/theme_2026-11-02_v1/`.

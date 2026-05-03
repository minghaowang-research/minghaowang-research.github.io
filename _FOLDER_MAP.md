# Folder Map

Last updated: 2026-05-02

---

## Root

| File | Purpose |
|---|---|
| CLAUDE.md | Universal rules + project context + tracking rules |
| _CHANGELOG.md | File operations log |
| _FOLDER_MAP.md | This file |
| _Archive/ | File snapshots before edits |
| _config.yml | Jekyll site config (author, collections, plugins, GA4) |
| _config_docker.yml | Docker override (blanks url for local dev) |
| Gemfile | Ruby dependencies |
| package.json | npm build scripts (JS bundling) |
| Dockerfile | Local dev container |
| docker-compose.yaml | Local dev container |
| .gitignore | Git ignore rules |
| googleb4efc3d3a7e1a98d.html | Google Search Console verification |
| LICENSE | MIT license (from Academic Pages) |

---

## _pages/

| File | Purpose |
|---|---|
| about.md | Homepage (permalink: /) - biography, education, awards, CV download link |
| research.md | Research page - working papers, conferences, service |
| teaching.md | Teaching page - courses, philosophy, certifications |
| travel.md | Photography & travel page |
| 404.md | Custom 404 page |

---

## _teaching/

| File | Purpose |
|---|---|
| marketing-327.md | MKT 327 course page (all years) |
| 2025-summer-cep-820.md | CEP 820 course page |
| 2025-summer-cola.md | COLA 2025 conference presentation |
| certification-college-teaching.md | CCT ePortfolio page |
| course-communication-policy.md | Course communication policy |
| teaching-philosophy.md | Teaching philosophy statement |

---

## _data/

| File | Purpose |
|---|---|
| navigation.yml | Top nav links (Research, Teaching, Travel) |
| ui-text.yml | UI string translations (theme file) |

---

## files/

| File | Purpose |
|---|---|
| Minghao-Wang-PhD-CV.pdf | Current CV |
| 2025-summer-mkt327-syllabus.pdf | MKT 327 syllabus |

### files/CCTI/ (13 PDFs)

| File | Purpose |
|---|---|
| MSU_CCT_Certification_2025.pdf | CCT certificate |
| 1_CCT_Institute_2025_Receipt.pdf | CCT receipt |
| 2_CCT_Portfolio_Checklist_Minghao_Wang.pdf | Portfolio checklist |
| 3_Competency_1_CEP_820_4_0.pdf | Competency 1 evidence |
| 4_Competency_2_and_3.pdf | Competency 2 & 3 evidence |
| 5_Competency_4.pdf | Competency 4 evidence |
| 6_Competency_5_Mentored_Project_Worksheet_Minghao.pdf | Comp 5 worksheet |
| 7_Competency_5_Mentored_Teaching_Project_Document_Graduate_Student_Minghao.pdf | Comp 5 project doc |
| 8_Competency_5_Summary_Artifacrs.pdf | Comp 5 summary |
| 9_Re_Sharing_your_professional_website.pdf | Website sharing email |
| 10_TEACHING_PHILOSOPHY_STATEMENT_Minghao.pdf | Teaching philosophy PDF |
| 11_US25-MKT-327-734_Pre.pdf | Pre-evaluation |
| 12_US25-MKT-327-734_Mid.pdf | Mid-evaluation |

---

## images/

| File | Purpose |
|---|---|
| profile.png | Author sidebar photo |
| favicon.ico | Favicon |
| favicon.svg | Favicon SVG |
| favicon-32x32.png | Favicon 32px |
| favicon-192x192.png | Favicon 192px |
| favicon-512x512.png | Favicon 512px |
| apple-touch-icon-180x180.png | Apple touch icon |
| manifest.json | Web app manifest for favicons |
| homepage.png | Homepage screenshot |
| themes/homepage-dark.png | Dark theme screenshot |
| themes/homepage-light.png | Light theme screenshot |

---

## appendix/ (convention - currently empty)

Not currently on disk. When needed, create `appendix/<project-name>/` for web-viewable supplementary content (HTML appendices, survey PDFs, etc.).
URL pattern: `minghaowang-research.github.io/appendix/<project-name>/filename.htm`

Previous content (mkt-902-912-spring2025, 7 files) removed 2026-05-02; recoverable from git history.

---

## assets/

| File / Folder | Purpose |
|---|---|
| css/main.scss | Main stylesheet entry point |
| css/academicons.css | Academicons CSS |
| css/academicons.min.css | Academicons CSS (minified) |
| css/collapse.css | Collapsible section CSS |
| js/main.min.js | Bundled JS (jQuery + plugins) |
| js/_main.js | Pre-bundle JS source |
| js/collapse.js | Collapsible section JS |
| js/plugins/jquery.greedy-navigation.js | Greedy nav plugin |
| fonts/ (4 files) | Academicon font files (eot, svg, ttf, woff) |
| webfonts/ (8 files) | Font Awesome 6 webfonts |

---

## _sass/ (theme SCSS)

| File / Folder | Purpose |
|---|---|
| _syntax.scss | Syntax highlighting |
| _themes.scss | Theme imports |
| include/ (2 files) | Mixins and utilities |
| layout/ (12 files) | Page layout styles |
| theme/ (2 files) | Default and dark theme variables |
| vendor/ | Third-party: breakpoint, font-awesome, magnific-popup, susy |

---

## _includes/ (30+ files)

Template partials: analytics, author-profile, comments, footer, head, masthead, sidebar, SEO, scripts, pagination, etc.

---

## _layouts/ (7 files)

| File | Purpose |
|---|---|
| default.html | Base layout |
| single.html | Single page/post |
| archive.html | Archive listing |
| archive-taxonomy.html | Category/tag archive |
| splash.html | Splash page |
| talk.html | Talk page |
| compress.html | HTML compression |

---

## _Archive/_pages/

| File | Purpose |
|---|---|
| cv_2026-05-02_v1.md | Snapshot before graduation year fix |
| cv_2026-05-02_v2.md | Final version before removal |
| travel_2026-05-02_v1.md | Snapshot before country/park lists added |
| teaching_2026-05-02_v1.md | Snapshot before 2026 MKT 327 added |
| teaching_2026-05-02_v2.md | Snapshot before MKT 327 merge to single page |

## _Archive/ (other)

| File | Purpose |
|---|---|
| mapchartSave__world_advanced__2026-05-02.txt | Mapchart.net save file with 49 countries/territories |

## _Archive/_teaching/

| File | Purpose |
|---|---|
| 2025-summer-marketing-327_2026-05-02_v1.md | Snapshot before rating moved from title to body |
| 2025-summer-marketing-327_2026-05-02_v2.md | Final version before merge into marketing-327.md |
| 2026-summer-marketing-327_2026-05-02_v1.md | Final version before merge into marketing-327.md |

---

## .claude/

| File | Purpose |
|---|---|
| settings.local.json | Claude Code local settings |

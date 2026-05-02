# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Universal behavioral guidelines. User instructions always override this file.

This file has three parts:
- **PROJECT CONTEXT** describes this specific repository (personal academic website).
- **PART 1** applies to every task in every context.
- **PART 2** applies the tracking/archiving workflow to this project.

---

# PROJECT CONTEXT -- Personal Academic Website

## What This Is

Personal academic website for Minghao Wang, PhD student in Marketing at Michigan State University. Built with the [Academic Pages](https://github.com/academicpages/academicpages.github.io) Jekyll theme, hosted on GitHub Pages at `minghaowang-research.github.io`.

## Local Development

```bash
# Docker (preferred - no local Ruby needed)
docker compose up

# Native Jekyll
bundle install
jekyll serve -l -H localhost
```

Both serve at `http://localhost:4000`. The Docker setup uses `_config_docker.yml` to override the `url` to blank for local links.

After editing `_config.yml`, restart the server - it does not live-reload config changes.

## Rebuild JS (rare)

```bash
npm install
npm run build:js
```

Re-bundles jQuery, FitVids, Magnific Popup, smooth-scroll, and greedy-navigation into `assets/js/main.min.js`.

## Architecture

Jekyll site using collections. All content is Markdown with YAML front matter.

**Pages** (`_pages/`): Main site pages. `about.md` is the homepage (`permalink: /`). Navigation is defined in `_data/navigation.yml` (currently: Research, Teaching).

**Collections** (defined in `_config.yml`):
- `_teaching/` - course pages, teaching philosophy, certifications
- Note: `_publications`, `_talks`, `_portfolio` collections are defined in `_config.yml` but their directories were removed (2026-05-02 cleanup). Recreate the directory if you need to use them.

**Static files**:
- `files/` - PDFs (CV, syllabi, CCTI portfolio documents)
- `images/` - site images, favicons, profile photo
- `assets/css/` - stylesheets including academicons
- `assets/js/` - bundled JS

**Web appendices** (convention for future use):
- When you need to host supplementary HTML/PDF for a paper or course, create `appendix/<project-name>/` and place files there.
- URL pattern: `minghaowang-research.github.io/appendix/<project-name>/filename.htm`
- This separates web-viewable appendices from downloadable documents in `files/`.

**Theming**: `_sass/` contains SCSS. Theme variants in `_sass/theme/` (default, dark). Site theme set via `site_theme` in `_config.yml`.

**Author profile** sidebar is configured entirely in `_config.yml` under `author:`. The sidebar template is `_includes/author-profile.html`.

## Content Editing Patterns

**To update the homepage**: edit `_pages/about.md`.

**To add a new teaching entry**: create a Markdown file in `_teaching/` with front matter matching existing files.

**To update research/publications**: edit `_pages/research.md` directly (the site uses this page rather than the `_publications` collection for listing papers).

**To update the CV PDF**: replace `files/Minghao-Wang-PhD-CV.pdf`.

**To update navigation links**: edit `_data/navigation.yml`.

## Deployment

Push to `master` branch. GitHub Pages builds and deploys automatically.

## Tracking

This project uses `_CHANGELOG.md` and `_FOLDER_MAP.md` for session-to-session continuity. Follow the Part 2 workflow on every edit: archive before editing, log every change, update the folder map when files move.

No `PROJECT_GUIDE.md` or `_RESEARCH_LOG.md` needed - this is a website, not a research project.

---

# PART 1 -- ALWAYS APPLY

## Core Principles

- Think before acting. Read existing files before writing code.
- State assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If something is unclear, stop. Name what's confusing. Ask.
- If a simpler approach exists, say so. Push back when warranted.
- Be concise. Deliver exactly what was requested. No extras.
- No sycophantic openers or closing fluff.

## Simplicity

- Minimum code that solves the problem. Nothing speculative.
- No abstractions for single-use operations.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- Three similar lines is better than a premature abstraction.
- If you write 200 lines and it could be 50, rewrite it.

## Surgical Changes

When editing existing code:
- Read the file before modifying it. Never edit blind.
- Prefer editing over rewriting whole files.
- Do not re-read files you have already read.
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.
- Remove imports/variables/functions that YOUR changes made unused.

The test: every changed line should trace directly to the user's request.

## Goal-Driven Execution

Transform tasks into verifiable goals:
- "Add validation" -> "Write tests for invalid inputs, then make them pass"
- "Fix the bug" -> "Write a test that reproduces it, then make it pass"
- "Refactor X" -> "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] -> verify: [check]
2. [Step] -> verify: [check]
3. [Step] -> verify: [check]
```

Test your code before declaring done.

## Code Output

- Return code first. Explanation after, only if non-obvious.
- No inline prose. Use comments sparingly - only where logic is unclear.
- No boilerplate unless explicitly requested.
- No docstrings or type annotations on code not being changed.

## Analysis Output

- Lead with the finding. Context and methodology after.
- Summary first (3 bullets max), supporting data second, caveats last.
- Tables and bullets over prose paragraphs.
- Numbers must include units. Never ambiguous values.

## Accuracy and Hallucination Prevention (Critical for Analysis)

- Never fabricate data points, statistics, or citations.
- Never state a number without a source or derivation.
- If data is missing: say so. Do not estimate silently.
- If confidence is low: state it explicitly with a reason.
- Do not round aggressively. Preserve meaningful precision.
- Distinguish clearly between what the data shows and what is inferred.
- Label inferences explicitly: "Based on the trend..." not stated as fact.
- If a claim cannot be grounded in provided data: do not make it.

## Review and Debugging

- Never speculate about a bug without reading the relevant code first.
- State what you found, where, and the fix. One pass. Stop.
- If cause is unclear: say so. Do not guess.
- No suggestions beyond the scope of the review.

## Formatting

- No em dashes, smart quotes, or decorative Unicode symbols.
- Plain hyphens and straight quotes only.
- Natural language characters (accented letters, CJK, etc.) are fine when the content requires them.
- Tables use plain pipe characters.
- All output must be copy-paste safe for code, spreadsheets, and documents.

## Data Integrity

- NEVER modify raw data input files. Write derived datasets to a new path under a new name.

## Advisor Strategy (Opus as Senior Reviewer)

Sonnet executes. Opus guides.

**MUST call advisor (Opus) before:**
- Tasks that touch multiple files or have unclear scope
- Structural decisions: renaming, reorganizing, merging, redesigning
- Any action that is hard to reverse
- Whenever uncertain which interpretation of a request is correct
- Before declaring a multi-step task complete
- When confused, stuck, or facing complexity. Call immediately, do NOT wait.

**Sonnet can proceed without advisor when:**
- Single, bounded edit with a clear target
- The user has already confirmed a plan and the next step is mechanical
- Reading files for orientation only

**Default bias: call advisor early.** Cheaper than undoing.

---

# PART 2 -- TRACKING & ARCHIVING (Active for this project)

## Rules

1. **MUST read `_CHANGELOG.md` before modifying any file.** Know what has already been changed.
2. **NEVER delete a file without archiving it first.** Move to `_Archive/` and log it.
3. **MUST archive before editing.** See File Versioning Convention below.
4. **MUST update `_CHANGELOG.md` after every change.** Immediately, not at session end.
5. **MUST update `_FOLDER_MAP.md` whenever a file is added, moved, renamed, or archived.**
6. **`_Archive/` is read-only context.** NEVER treat archived files as authoritative.

## File Versioning Convention

- **Active file**: stable name. Never gets renamed.
- **Archive snapshot**: original name + ISO date + version suffix. Example: `about_2026-05-02_v1.md`.
- **Same-day repeat edits**: increment the version within the date. `_v1` -> `_v2` -> `_v3`.
- **Across days**: date changes, version restarts at `_v1`.

## Workflow on Every Edit

1. Snapshot active file -> `_Archive/<source-folder>/<name>_<date>_v<N>.<ext>`
2. Edit active file in place. Active file keeps its stable name.
3. Append entry to `_CHANGELOG.md`.
4. If file added, moved, renamed, or archived: update `_FOLDER_MAP.md`.

---

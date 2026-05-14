---
layout: archive
title: "Tools & Software"
permalink: /tools/
author_profile: true
---

{% include base_path %}

Small tools I built for personal use and for fun.

## Scholar Journal Highlighter

A Chrome extension for business school researchers that highlights top-tier academic journals directly on Google Scholar search results and author profile pages.

**Features:**
- Visual tier badges for UTD24, FT50, and ABDC (A\*/A) journal lists
- Profile summary bar showing publication counts per list, with click-to-filter
- Three display modes: show all, dim non-matches, or hide non-matches
- Custom journal list with CSV/XLSX import and export
- Library proxy integration for one-click institutional access
- Citation count highlighting (100+, 500+, 1000+ papers)
- Colorblind-safe, WCAG AA-compliant design

Built with JavaScript as a Chrome Manifest V3 extension.

[View on GitHub](https://github.com/minghaowang-research/scholar-journal-highlighter){: .btn .btn--primary}

---

## MSU Menu Emailer

An automated daily email service that delivers Michigan State University dining hall menus to subscribers each morning at 7 AM Eastern.

**Features:**
- Covers all major dining halls (Brody, The Gallery, Kellogg, and more)
- Highlights special items (steak, fish, seafood) in a summary box at the top
- Shows which halls are open or closed with date ranges
- Organizes meals by time (breakfast, lunch, dinner) with station-level detail
- Dietary preference badges (vegetarian, vegan)
- Privacy-preserving BCC delivery
- Easy subscriber management via GitHub - just edit a text file
- Runs automatically via GitHub Actions (no server needed)

Built with Python. Uses BeautifulSoup for web scraping, Gmail SMTP for delivery, and GitHub Actions for scheduling.

[View on GitHub](https://github.com/minghaowang-research/msu-menu-emailer){: .btn .btn--primary}

---
layout: archive
title: "Teaching & Teaching Philosophy"
permalink: /teaching/
author_profile: true
---

{% include base_path %}

## Teaching Philosophy

{% for post in site.teaching reversed %}
  {% if post.categories contains 'teaching-philosophy' %}
**[{{ post.title }}]({{ base_path }}{{ post.permalink }})**
  {% endif %}
{% endfor %}

## Teaching Experience

{% for post in site.teaching reversed %}
  {% if post.categories contains 'teaching-experience' %}
**[{{ post.title }}]({{ base_path }}{{ post.permalink }})**  
{{ post.type }}, *{{ post.venue }}*, {{ post.date | date: "%Y" }}
  {% endif %}
{% endfor %}

## Professional Development in Teaching & Teaching Manifesto

{% for post in site.teaching reversed %}
  {% if post.categories contains 'professional-development' %}
**[{{ post.title }}]({{ base_path }}{{ post.permalink }})**  
{{ post.type }}, *{{ post.venue }}*, {{ post.date | date: "%Y" }}
  {% endif %}
{% endfor %}

<!-- Add concise entries for quick index visibility -->
**[Certification in College Teaching Institute (CCTI)]({{ base_path }}/teaching/certification-college-teaching)**  
Professional Development Certification, *Michigan State University*, 2025

**[COLA: Colleges' Online Learning Academy Fellowship]({{ base_path }}/teaching/2025-summer-cola)**  
Professional Development Fellowship, *Michigan State University*, 2025

**[CEP 820: Teaching and Learning Online (My Teaching Manifesto)]({{ base_path }}/teaching/2025-summer-cep-820)**  
Graduate course, *Michigan State University*, 2025

## Technical Skills for Teaching

* **Data Analysis Tools**: R, Python, SPSS & SPSS Modeler, Stata, Tableau
* **Business Analytics**: Arena, @Risk, Qualtrics
* **Database Management**: SQL
* **Market Research Resources**: Mintel, Passport, Fitch, MarketLine
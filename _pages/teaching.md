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
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

## Teaching Experience

{% for post in site.teaching reversed %}
  {% if post.categories contains 'teaching-experience' %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

## Classes Have Taken

{% for post in site.teaching reversed %}
  {% if post.categories contains 'classes-taken' %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

## Technical Skills for Teaching

* **Data Analysis Tools**: R, Python, SPSS & SPSS Modeler, Stata, Tableau
* **Business Analytics**: Arena, @Risk, Qualtrics
* **Database Management**: SQL
* **Market Research Resources**: Mintel, Passport, Fitch, MarketLine
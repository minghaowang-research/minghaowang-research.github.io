---
layout: archive
title: "Teaching & Teaching Philosophy"
permalink: /teaching/
author_profile: true
---

{% include base_path %}

{% for post in site.teaching reversed %}
  {% if post.categories contains 'teaching-philosophy' %}
[{{ post.title }}]({{ base_path }}{{ post.permalink }})
  {% endif %}
{% endfor %}

## Teaching Experience

{% for post in site.teaching reversed %}
  {% if post.categories contains 'teaching-experience' %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

## Professional Development in Teaching

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
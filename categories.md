---
layout: page
title: Categories
permalink: /categories/
---

{% comment %} 
  对分类名称进行字母排序，使展示更有序。
  site.categories 是一个哈希表，遍历时 category[0] 为分类名，category[1] 为文章数组。
{% endcomment %}

{% assign sorted_categories = site.categories | sort %}

{% for category in sorted_categories %}
  {% assign category_name = category[0] %}
  {% assign posts = category[1] %}

  <h2 id="{{ category_name | slugify }}">{{ category_name }}</h2>
  
  <ul class="post-list">
    {% for post in posts %}
      <li>
        <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>
        <h3>
          <a class="post-link" href="{{ post.url | relative_url }}">
            {{ post.title | escape }}
          </a>
        </h3>
      </li>
    {% endfor %}
  </ul>
  
{% endfor %}
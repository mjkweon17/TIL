---
layout: default
title: index.md
---

<h1>최근 포스트</h1>

<ul>
  {% raw %}{% for post in site.posts %}{% endraw %}
    <li>
      <a href="{% raw %}{{ post.url }}{% endraw %}">{% raw %}{{ post.title }}{% endraw %}</a>
      <span>{% raw %}{{ post.date | date: "%Y-%m-%d" }}{% endraw %}</span>
    </li>
  {% raw %}{% endfor %}{% endraw %}
</ul>
---
title: Slides
---

{% for talk in site.talks %}
  <h2>
    <a href="{{ talk.url | relative_url }}">
      {{ talk.slug }}
    </a>
  </h2>
{% endfor %}

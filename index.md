---
layout: default
title: Home
---

<div class="project-grid">
  {% for project in site.data.projects %}
    <div class="project-item">
      <a href="{{ project.url | relative_url }}">
        <img src="{{ project.thumbnail | relative_url }}" alt="{{ project.title }}" loading="lazy">
        <div class="project-info">
          <h3>{{ project.title }}</h3>
          <p>{{ project.description }}</p>
        </div>
      </a>
    </div>
  {% endfor %}
</div>

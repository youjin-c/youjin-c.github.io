---
layout: default
title: Home
---

<div class="project-grid">
  {% for project in site.data.projects %}
    <div class="project-item">
      <a href="{{ project.url | relative_url }}">
        <img src="{{ project.thumbnail | relative_url }}" alt="{{ project.title }}">
        <h3>{{ project.title }}</h3>
      </a>
      <p>{{ project.description }}</p>
    </div>
  {% endfor %}
</div>

<style>
  .project-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 20px;
    padding: 20px;
  }
  .project-item {
    border: 1px solid #ddd;
    padding: 15px;
    text-align: center;
    box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
  }
  .project-item img {
    max-width: 100%;
    height: auto;
    margin-bottom: 10px;
  }
  .project-item h3 {
    margin-top: 0;
    font-size: 1.2em;
  }
  .project-item p {
    font-size: 0.9em;
    color: #555;
  }
</style>
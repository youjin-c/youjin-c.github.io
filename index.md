---
layout: default
title: Home
---

<div class="tabs">
  <button class="tab-btn active" data-tab="project">Projects</button>
  <button class="tab-btn" data-tab="blog">Blog</button>
</div>

<div class="project-grid" id="project-grid">
  {% for project in site.data.projects %}
    <div class="project-item" data-category="{{ project.category }}">
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

<script>
document.addEventListener('DOMContentLoaded', function() {
  const tabs = document.querySelectorAll('.tab-btn');
  const items = document.querySelectorAll('.project-item');

  function filterProjects(category) {
    items.forEach(item => {
      if (category === 'all' || item.dataset.category === category) {
        item.style.display = 'block';
      } else {
        item.style.display = 'none';
      }
    });
  }

  tabs.forEach(tab => {
    tab.addEventListener('click', function() {
      tabs.forEach(t => t.classList.remove('active'));
      this.classList.add('active');
      filterProjects(this.dataset.tab);
    });
  });

  // Initial filter
  filterProjects('project');
});
</script>

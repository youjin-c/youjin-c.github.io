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
  const grid = document.getElementById('project-grid');
  const items = document.querySelectorAll('.project-item');
  const gap = 24; // 1.5rem in pixels

  function getColumnCount() {
    const width = window.innerWidth;
    if (width <= 600) return 1;
    if (width <= 1000) return 2;
    if (width <= 1400) return 3;
    return 4;
  }

  function layoutMasonry() {
    const cols = getColumnCount();
    const colHeights = new Array(cols).fill(0);
    const containerWidth = grid.offsetWidth;
    const colWidth = (containerWidth - gap * (cols - 1)) / cols;

    let visibleItems = Array.from(items).filter(item => item.style.display !== 'none');

    // Row-first ordering: assign items to shortest column, but prefer left-to-right
    visibleItems.forEach((item, index) => {
      // Find the column with minimum height (prefer leftmost if tie)
      let minHeight = Math.min(...colHeights);
      let col = colHeights.indexOf(minHeight);

      const x = col * (colWidth + gap);
      const y = colHeights[col];

      item.style.left = x + 'px';
      item.style.top = y + 'px';
      item.style.width = colWidth + 'px';

      colHeights[col] += item.offsetHeight + gap;
    });

    // Set container height
    grid.style.height = Math.max(...colHeights) + 'px';
  }

  function filterProjects(category) {
    items.forEach(item => {
      if (category === 'all' || item.dataset.category === category) {
        item.style.display = 'block';
      } else {
        item.style.display = 'none';
      }
    });
    // Wait for images to load, then layout
    setTimeout(layoutMasonry, 100);
  }

  tabs.forEach(tab => {
    tab.addEventListener('click', function() {
      tabs.forEach(t => t.classList.remove('active'));
      this.classList.add('active');
      filterProjects(this.dataset.tab);
    });
  });

  // Handle resize
  window.addEventListener('resize', layoutMasonry);

  // Initial filter and layout
  filterProjects('project');

  // Re-layout after all images loaded
  window.addEventListener('load', layoutMasonry);
});
</script>

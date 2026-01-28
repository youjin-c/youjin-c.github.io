---
layout: project
title: Posture & Eye Care
---

# Posture & Eye Care

<p style="text-align: right;"><em><strong><a href="https://github.com/youjinChung/PostureEyeCare">GitHub Repo</a></strong></em><br><em>LG Electronics</em></p>

![](images/POSTURE-EYE-CARE/ARCHIVEE22_o_1.jpg)

Healthcare web application for PC/laptop users.
It tracks user facial position and eye blink.
Through its algorithm and calculation, it encourages the user to adjust their
working posture and frequently blink to prevent slouching and dry eye
syndrome.

<div class="image-carousel-wrapper">
<div class="image-carousel" id="postureCarousel">
  <div class="carousel-track">
    <img src="/images/POSTURE-EYE-CARE/-2015-12-30--4.31.13.png" alt="Posture Eye Care 1">
    <img src="/images/POSTURE-EYE-CARE/-2015-12-30--4.40.48.png" alt="Posture Eye Care 2">
    <img src="/images/POSTURE-EYE-CARE/-2015-12-30--4.41.59.png" alt="Posture Eye Care 3">
    <img src="/images/POSTURE-EYE-CARE/-2015-12-30--4.42.17.png" alt="Posture Eye Care 4">
    <img src="/images/POSTURE-EYE-CARE/-2015-12-30--4.41.20.png" alt="Posture Eye Care 5">
    <img src="/images/POSTURE-EYE-CARE/-2015-12-30--4.43.23.png" alt="Posture Eye Care 6">
    <img src="/images/POSTURE-EYE-CARE/-2015-12-30--4.43.04.png" alt="Posture Eye Care 7">
    <img src="/images/POSTURE-EYE-CARE/-2015-12-30--4.43.42.png" alt="Posture Eye Care 8">
  </div>
  <button class="carousel-btn prev" onclick="movePostureCarousel(-1)">&lt;</button>
  <button class="carousel-btn next" onclick="movePostureCarousel(1)">&gt;</button>
  <div class="carousel-dots"></div>
</div>
</div>

<script>
(function() {
  const carousel = document.getElementById('postureCarousel');
  const track = carousel.querySelector('.carousel-track');
  const images = track.querySelectorAll('img');
  const dotsContainer = carousel.querySelector('.carousel-dots');
  let currentIndex = 0;
  const totalImages = images.length;
  let carouselWidth = 0;
  let isAnimating = false;

  function initCarousel() {
    let maxWidth = 0;
    images.forEach(img => {
      if (img.naturalWidth > maxWidth) maxWidth = img.naturalWidth;
    });
    carouselWidth = Math.min(maxWidth, carousel.parentElement.offsetWidth);
    carousel.style.width = carouselWidth + 'px';
    images.forEach(img => {
      img.style.width = carouselWidth + 'px';
    });
    updateCarousel();
  }

  let loadedCount = 0;
  images.forEach(img => {
    if (img.complete) {
      loadedCount++;
      if (loadedCount === totalImages) initCarousel();
    } else {
      img.onload = () => {
        loadedCount++;
        if (loadedCount === totalImages) initCarousel();
      };
    }
  });

  images.forEach((_, i) => {
    const dot = document.createElement('button');
    dot.className = 'carousel-dot' + (i === 0 ? ' active' : '');
    dot.onclick = () => goToSlide(i);
    dotsContainer.appendChild(dot);
  });

  function updateCarousel() {
    track.style.transform = `translateX(-${currentIndex * carouselWidth}px)`;
    const dots = dotsContainer.querySelectorAll('.carousel-dot');
    dots.forEach((dot, i) => dot.classList.toggle('active', i === currentIndex));
  }

  window.movePostureCarousel = function(direction) {
    if (isAnimating) return;
    isAnimating = true;
    currentIndex = (currentIndex + direction + totalImages) % totalImages;
    updateCarousel();
    setTimeout(() => { isAnimating = false; }, 500);
  };

  function goToSlide(index) {
    if (isAnimating || index === currentIndex) return;
    isAnimating = true;
    currentIndex = index;
    updateCarousel();
    setTimeout(() => { isAnimating = false; }, 500);
  }

  setInterval(() => movePostureCarousel(1), 4000);
})();
</script>

## System

Javascript, HTML, CSS, LG face recognition ML engine

Web Application Development implemented for LG Chromebase, Chrome web browser, Chrome OS

## Role

Ideation, research, implementation, programming

---
layout: project
title: Smile Face-in
---

# Smile Face-in

<p style="text-align: right;"><em>LG Electronics</em></p>

![](images/SMILE-FACE-IN/ARCHIVEE24_o_1.jpg)

LG laptop Gram User Identification System  
Users can sign in their OS using face recognition, without typing ID and PW
every time. It prevents authentication using stolen photos by encouraging
natural changes in facial expressions.  


<div class="image-carousel-wrapper">
<div class="image-carousel" id="smileFaceinCarousel">
  <div class="carousel-track">
    <img src="/images/SMILE-FACE-IN/lg_face_in_2_01.gif" alt="Smile Face-in 1">
    <img src="/images/SMILE-FACE-IN/lg_face_in_2_02.gif" alt="Smile Face-in 2">
    <img src="/images/SMILE-FACE-IN/lg_face_in_2_03.gif" alt="Smile Face-in 3">
    <img src="/images/SMILE-FACE-IN/lg_face_in_2_04.gif" alt="Smile Face-in 4">
    <img src="/images/SMILE-FACE-IN/lg_face_in_2_05.gif" alt="Smile Face-in 5">
    <img src="/images/SMILE-FACE-IN/lg_face_in_2_06.gif" alt="Smile Face-in 6">
  </div>
  <button class="carousel-btn prev" onclick="moveSmileFaceinCarousel(-1)">&lt;</button>
  <button class="carousel-btn next" onclick="moveSmileFaceinCarousel(1)">&gt;</button>
  <div class="carousel-dots"></div>
</div>
</div>

<script>
(function() {
  const carousel = document.getElementById('smileFaceinCarousel');
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

  window.moveSmileFaceinCarousel = function(direction) {
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

  setInterval(() => moveSmileFaceinCarousel(1), 4000);
})();
</script>

## System  

C, C++, LG face recognition ML engine  
  
Windows Service Developmen  
Implemented for LG Gram laptop  
  

## Role

Ideation, Research, Algorithm
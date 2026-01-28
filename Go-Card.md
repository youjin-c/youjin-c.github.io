---
layout: project
title: Go Card
---

# Go Card

<p style="text-align: right;"><em><strong><a href="https://github.com/youjinChung/GoCard">GitHub Repo</a></strong></em><br><em>NYU ITP project</em></p>

<iframe src="https://player.vimeo.com/video/294069117" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>

<div class="image-carousel-wrapper">
<div class="image-carousel" id="gocardCarousel">
  <div class="carousel-track">
    <img src="/images/Go-Card/gocard0.jpg" alt="Go Card 1">
    <img src="/images/Go-Card/gocard1.jpg" alt="Go Card 2">
    <img src="/images/Go-Card/1.jpg" alt="Go Card 3">
    <img src="/images/Go-Card/2.jpg" alt="Go Card 4">
    <img src="/images/Go-Card/3.jpeg" alt="Go Card 5">
  </div>
  <button class="carousel-btn prev" onclick="moveGocardCarousel(-1)">&lt;</button>
  <button class="carousel-btn next" onclick="moveGocardCarousel(1)">&gt;</button>
  <div class="carousel-dots"></div>
</div>
</div>

<script>
(function() {
  const carousel = document.getElementById('gocardCarousel');
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

  window.moveGocardCarousel = function(direction) {
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

  setInterval(() => moveGocardCarousel(1), 4000);
})();
</script>

Go Card is a concept of language education kit.  
The Korean letters are written in syllabic blocks with each alphabetic letter
placed vertically and horizontally into a square dimension. Using that
characteristic, we designed an education kit for learning Korean letters.  
We chose “ㄱ" + “ㅏ” = “가“, 가 is the most simple and basic letter when you learn
Korean as we learn A, B, C in English. 가 also has a meaning of ‘Go’, so we
named our kit as Go Card.  
  

## System  
![](images/Go-Card/gocard2.jpg)

Each vowel and the consonant card has its own sound. The user can hear them
when they press the card on the kit.  
When they stack the cards together, they can learn how the consonant and the
vowel combine to make a sound.  
  
The kit is designed with acrylic sheet and conductive paint, and an Arduino
board. Programmed with P5.js.  
Using the different lenght of each letter's stroke, we designed each sound
'ㄱ', 'ㅏ', and '가' to have different resistance.

<iframe src="https://player.vimeo.com/video/294069607" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>

## Role

Ideation, Design, Programming  
  

## Credit

[Dongphil Yoo](http://dongphilyoo.com): Ideation, Fabrication, Documentaion
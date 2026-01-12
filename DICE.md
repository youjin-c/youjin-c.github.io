---
layout: project
title: DICE
---

_**[Github Repo](https://github.com/youjinChung/DICE)**_  
Featured at Reykjavik Winter Festival 2019

<iframe src="https://player.vimeo.com/video/318835829" allowfullscreen></iframe>

<div class="image-carousel-wrapper">
<div class="image-carousel" id="diceCarousel">
  <div class="carousel-track">
    <img src="/images/DICE/dice0.jpg" alt="DICE installation 1">
    <img src="/images/DICE/dice1.jpg" alt="DICE installation 2">
    <img src="/images/DICE/dice2.jpg" alt="DICE installation 3">
    <img src="/images/DICE/dice3.jpg" alt="DICE installation 4">
    <img src="/images/DICE/dice5.jpg" alt="DICE installation 5">
    <img src="/images/DICE/dice6.jpg" alt="DICE installation 6">
    <img src="/images/DICE/dice7.jpg" alt="DICE installation 7">
  </div>
  <button class="carousel-btn prev" onclick="moveDiceCarousel(-1)">&lt;</button>
  <button class="carousel-btn next" onclick="moveDiceCarousel(1)">&gt;</button>
  <div class="carousel-dots"></div>
</div>
</div>

<script>
(function() {
  const carousel = document.getElementById('diceCarousel');
  const track = carousel.querySelector('.carousel-track');
  const images = track.querySelectorAll('img');
  const dotsContainer = carousel.querySelector('.carousel-dots');
  let currentIndex = 0;
  const totalImages = images.length;
  let carouselWidth = 0;

  function initCarousel() {
    const firstImg = images[0];
    carouselWidth = firstImg.offsetWidth || firstImg.naturalWidth;
    if (carouselWidth > 0) {
      carousel.style.width = carouselWidth + 'px';
      images.forEach(img => {
        img.style.width = carouselWidth + 'px';
      });
    }
  }

  // Handle both cached and fresh images
  if (images[0].complete) {
    initCarousel();
  } else {
    images[0].onload = initCarousel;
  }

  images.forEach((_, i) => {
    const dot = document.createElement('button');
    dot.className = 'carousel-dot' + (i === 0 ? ' active' : '');
    dot.onclick = () => goToSlide(i);
    dotsContainer.appendChild(dot);
  });

  function updateCarousel() {
    if (carouselWidth === 0) initCarousel();
    track.style.transform = `translateX(-${currentIndex * carouselWidth}px)`;
    const dots = dotsContainer.querySelectorAll('.carousel-dot');
    dots.forEach((dot, i) => dot.classList.toggle('active', i === currentIndex));
  }

  window.moveDiceCarousel = function(direction) {
    currentIndex = (currentIndex + direction + totalImages) % totalImages;
    updateCarousel();
  };

  function goToSlide(index) {
    currentIndex = index;
    updateCarousel();
  }

  setInterval(() => moveDiceCarousel(1), 4000);
})();
</script>

Dice is an interactive light/music installation, which is award-winning work at Tiny Massive, Reykjavìk, Iceland.<br>
The project was shown during Reykjavìk Winter Festival, 2019.<br>
The audience and enjoy visual and audio interaction with the mapped game on Harpa.<br>

## System

[Playable Online Demo](https://youjin-c.github.io/DICEdemo/index.html)

The DICE music system is using [Markov
Chain](https://en.wikipedia.org/wiki/Markov_chain). On top of the base drum
line, the player can adjust probabilities of the main sample audios.

Magenta - 0%<br>
Green - 50%<br>
Blue - 100%<br>

For each loop, DICE have randomly generated probability, and it determines whether each sample will be played or not.<br>
The player2 can change the probability of each die, and the music will be played on the next loop. The player1 can change the color of the background particle and the speed of it.<br>
We used Unity3D to express 3D texture on the 2D LED surface on Harpa.<br>
The 3D visual is appreciated as a new approach to Harpa surface.<br>

![](images/DICE/dice_0.jpg)

<img src="images/DICE/giphy_1.gif" style="width: 200%;">

![](images/DICE/dice_2.jpg)

![](images/DICE/dice_3.jpg)

<iframe src="https://player.vimeo.com/video/318837289" allowfullscreen></iframe>

## Role

Unity 3D programming: Audio System, Markov Chain System on Cubes, Visual Effect

## Credit

[Dongphil Yoo](http://dongphilyoo.com/): Art Direct, Visual Allignment in Unity 3D, Documentation <br>
[Joohyun Park](https://www.parkjoohyun.com/): Concept, Music
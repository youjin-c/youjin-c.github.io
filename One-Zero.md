---
layout: project
title: One Zero
---

# One Zero

<p style="text-align: right;"><em><strong><a href="https://github.com/youjinChung/OneZero">GitHub Repo</a></strong></em><br><em>Featured at ITP Spring Show 2018</em></p>

<iframe src="https://player.vimeo.com/video/319150219" allowfullscreen></iframe>

One Zero is Interactive Kinetic Art Installation.  
The project implies the coexistence of the human cognitive process and machine
perception.  
  
The red ball travels between two laptops and the bulb lights on when the ball
passes through right in the middle of the virtual world.  
The audience can move laptops back and forth, and their positions get updated
to the virtual world in real-time.  
The installation shows the trace of the red ball in mixed reality.  
  
This project is shown at ITP 2018 Spring Show.  
  

<div class="image-carousel-wrapper">
<div class="image-carousel" id="oneZeroCarousel">
  <div class="carousel-track">
    <img src="/images/One-Zero/onezero4.jpg" alt="One Zero installation 1">
    <img src="/images/One-Zero/onezero3.jpg" alt="One Zero installation 2">
    <img src="/images/One-Zero/onezero1.jpg" alt="One Zero installation 3">
    <img src="/images/One-Zero/one-zero5.jpg" alt="One Zero installation 4">
    <img src="/images/One-Zero/onezero2.jpg" alt="One Zero installation 5">
  </div>
  <button class="carousel-btn prev" onclick="moveOneZeroCarousel(-1)">&lt;</button>
  <button class="carousel-btn next" onclick="moveOneZeroCarousel(1)">&gt;</button>
  <div class="carousel-dots"></div>
</div>
</div>

<script>
(function() {
  const carousel = document.getElementById('oneZeroCarousel');
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

  window.moveOneZeroCarousel = function(direction) {
    currentIndex = (currentIndex + direction + totalImages) % totalImages;
    updateCarousel();
  };

  function goToSlide(index) {
    currentIndex = index;
    updateCarousel();
  }

  setInterval(() => moveOneZeroCarousel(1), 4000);
})();
</script>

<div class="side-by-side-images">
<img src="/images/One-Zero/audience.gif" alt="One Zero audience interaction">
<img src="/images/One-Zero/show.gif" alt="One Zero show">
</div>

## System

Unity 3D, Arduino, Ultrasonic, Bluetooth, I2C communication

![](images/One-Zero/diagram.png)  

Two ultrasonic sensors calculate the distances between each laptop and the
pole in the middle and send them to Arduino.  
The master Arduino board collects the positions of two walls and a ball in the
unity and controls the light bulb.  
Each Arduino communicates with their ultrasonic sensor and unity via
Bluetooth, and two Arduinos communicate with each other via I2C.  
Unity3D physics engine calculates the movement of the ball with the distance
information.  
  

## Role  

Ideation, System architecture, Programming (Arduino, Unity3D)  
  

## Credit

[Dongphil Yoo](http://dongphilyoo.com/): Concept, Fabrication
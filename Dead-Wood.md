---
layout: project
title: Dead Wood
---

# Dead Wood

<p style="text-align: right;"><em><strong><a href="https://github.com/youjinChung/DeadWood">GitHub Repo</a></strong></em> | <em><strong><a href="https://docs.google.com/document/d/e/2PACX-1vQOm5emDvuGNVrj26LrcXf8KmtOVZYLAbMtxnwIKdyYtV15GzW_Qawxv8D3-Re4gUQPfal7ShGyn82G/pub">Paper</a></strong></em><br><em>Featured at UCLA Design Media Arts Solo Show</em></p>

<div class="image-carousel-wrapper">
<div class="image-carousel" id="deadwood1Carousel">
  <div class="carousel-track">
    <img src="/images/Dead-Wood/youjin_img_1944.jpg" alt="Dead Wood 1">
    <img src="/images/Dead-Wood/youjin_img_1948.jpg" alt="Dead Wood 2">
    <img src="/images/Dead-Wood/youjin_img_1960.jpg" alt="Dead Wood 3">
    <img src="/images/Dead-Wood/youjin_img_1968.jpg" alt="Dead Wood 4">
    <img src="/images/Dead-Wood/youjin_img_1981.jpg" alt="Dead Wood 5">
    <img src="/images/Dead-Wood/youjin_img_1984.jpg" alt="Dead Wood 6">
    <img src="/images/Dead-Wood/youjin_img_1986.jpg" alt="Dead Wood 7">
    <img src="/images/Dead-Wood/youjin_img_1992.jpg" alt="Dead Wood 8">
  </div>
  <button class="carousel-btn prev" onclick="moveDeadwood1Carousel(-1)">&lt;</button>
  <button class="carousel-btn next" onclick="moveDeadwood1Carousel(1)">&gt;</button>
  <div class="carousel-dots"></div>
</div>
</div>

<script>
(function() {
  const carousel = document.getElementById('deadwood1Carousel');
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

  window.moveDeadwood1Carousel = function(direction) {
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

  setInterval(() => moveDeadwood1Carousel(1), 4000);
})();
</script>

This project is inspired by the murder of hitchBOT in Philadelphia. From the articles that state this accident as a murder, not vandalism, Dead Wood questions empathy and anthropomorphism. In the era of AI, both threat and understanding towards different entities are anthropomorphized. Humanity, as potential and current cyborgs, Dead Wood advocates the expansion of empathy. The empathy towards non-human, robotic, or artificial beings will mirror the empathy towards humanity.

<iframe src="https://player.vimeo.com/video/351863681" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>

<div class="image-carousel-wrapper">
<div class="image-carousel" id="deadwood2Carousel">
  <div class="carousel-track">
    <img src="/images/Dead-Wood/IMG_4459.JPG" alt="Dead Wood game 1">
    <img src="/images/Dead-Wood/IMG_4489.JPG" alt="Dead Wood game 2">
    <img src="/images/Dead-Wood/IMG_4558.JPG" alt="Dead Wood game 3">
    <img src="/images/Dead-Wood/IMG_4634.JPG" alt="Dead Wood game 4">
    <img src="/images/Dead-Wood/IMG_4641.JPG" alt="Dead Wood game 5">
    <img src="/images/Dead-Wood/IMG_4643.JPG" alt="Dead Wood game 6">
  </div>
  <button class="carousel-btn prev" onclick="moveDeadwood2Carousel(-1)">&lt;</button>
  <button class="carousel-btn next" onclick="moveDeadwood2Carousel(1)">&gt;</button>
  <div class="carousel-dots"></div>
</div>
</div>

<script>
(function() {
  const carousel = document.getElementById('deadwood2Carousel');
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

  window.moveDeadwood2Carousel = function(direction) {
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

  setInterval(() => moveDeadwood2Carousel(1), 4000);
})();
</script>

The show has two pieces. An interactive video game with an installed controller and a kinetic sculpture. In the game, the audience can see the "hands", representing humanity and chimera entities on the field. What the audience can do is destroy them and see the pixelized particles of the objects. More the player kills objects, more the world is glitched, and they will see Laozi's quote: "The usefulness of a pot comes from its emptiness."

<iframe src="https://player.vimeo.com/video/351863082" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>

<div class="side-by-side-images">
<img src="/images/Dead-Wood/IMG_4343.jpg" alt="Dead Wood installation">
<img src="/images/Dead-Wood/IMG_4404.jpg" alt="Dead Wood installation">
</div>

The kinetic installation is a servo-powered tree shape sculpture with 3D printed chimeras from the game piece. With the quote of the game, it represents the arbitrariness of anthropomorphism.

## System

Unity3D + Xbox controller as input<br>
Arduino, Motorshield and Servos + 3D printed sculptures

## Role

Concept, Programming, Art, Installation

## Credit

[Sanglim Han](http://sanglimhan.work/): 3D modeling<br>
Ji Yun Hwang: Photography
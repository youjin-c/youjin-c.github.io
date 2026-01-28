---
layout: project
title: Suprememe
---

# Suprememe

<p style="text-align: right;"><em><strong><a href="https://github.com/youjinChung/Suprememe">GitHub Repo</a></strong></em> | <em><strong><a href="https://www.instagram.com/suprememebot/">Instagram</a></strong></em><br><em>NYU ITP project</em></p>

<iframe src="https://player.vimeo.com/video/322192045" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>

Suprememe is an automated Instagram bot, which generates product and T-shirt
images of Supreme aesthetics.  
It collects random product, garment images and detects objects in the images
to put the Supreme box logo or graphics on them.  
From collecting images, detecting objects, compositing, to posting to the
Instagram account, every step is automated.  
  
This account, not only generating images but also being liked and followed
other accounts (who probably are not checking what they are liking at all,) is
the archive of supreme fandom itself.  

![](images/Suprememe/IMG_0681.PNG)

<div class="image-carousel-wrapper">
<div class="image-carousel" id="suprememeCarousel">
  <div class="carousel-track">
    <img src="/images/Suprememe/Screen-Shot-2019-03-05-at-4.45.48-AM.png" alt="Suprememe example 1">
    <img src="/images/Suprememe/51809910_318641562338330_8577123256388326845_n.jpg" alt="Suprememe example 2">
    <img src="/images/Suprememe/51906524_264920787753356_5267881817543424021_n.jpg" alt="Suprememe example 3">
    <img src="/images/Suprememe/52016682_1312328162241427_69337598878520614_n.jpg" alt="Suprememe example 4">
    <img src="/images/Suprememe/52029445_2352758524960148_4451706964184833488_n.jpg" alt="Suprememe example 5">
    <img src="/images/Suprememe/52047741_438404700265624_8313240200024626529_n.jpg" alt="Suprememe example 6">
    <img src="/images/Suprememe/52072793_407632946469823_8930449736324571097_n.jpg" alt="Suprememe example 7">
    <img src="/images/Suprememe/52106116_387199972112039_977342567209289273_n.jpg" alt="Suprememe example 8">
    <img src="/images/Suprememe/52371584_181270459523114_396634372260760599_n.jpg" alt="Suprememe example 9">
    <img src="/images/Suprememe/52450209_769012530142168_9083129169983605449_n.jpg" alt="Suprememe example 10">
    <img src="/images/Suprememe/52993959_153429738934399_738117296143646008_n.jpg" alt="Suprememe example 11">
    <img src="/images/Suprememe/53010814_388651265257198_5238490325053075448_n.jpg" alt="Suprememe example 12">
  </div>
  <button class="carousel-btn prev" onclick="moveSuprememeCarousel(-1)">&lt;</button>
  <button class="carousel-btn next" onclick="moveSuprememeCarousel(1)">&gt;</button>
  <div class="carousel-dots"></div>
</div>
</div>

<script>
(function() {
  const carousel = document.getElementById('suprememeCarousel');
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

  window.moveSuprememeCarousel = function(direction) {
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

  setInterval(() => moveSuprememeCarousel(1), 4000);
})();
</script>

## System

![](images/Suprememe/flowchart.png)

[Selenium](https://www.seleniumhq.org/),
[ImageAI](https://github.com/OlafenwaMoses/ImageAI/tree/master/imageai/Detection),
[InstagramAPI](https://github.com/LevPasha/Instagram-API-python),
[Pillow](https://pillow.readthedocs.io/en/stable/#)  
  
1\. It grabs images from websites: a product image from Alibaba, a white
T-shirt image from Google, a graphic image from Instagram(#glitch). All images
are chosen randomly.  
2\. It detects objects in a product image, or a T-shirt image, and choose one
object among them.  
3\. It puts the Supreme box logo if the chosen object is a product image or a
T-shirt image, or it puts a graphic image on the chosen T-shirt image.  
4\. It posts the composited image to [the Instagram
account.](https://www.instagram.com/suprememebot/)  
  

## Role

Concept, Programming
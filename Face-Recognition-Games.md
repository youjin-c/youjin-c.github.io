---
layout: project
title: Face Recognition Games
---

# Face Recognition Games

# Banksy in us

<p style="text-align: right;"><em><strong><a href="https://github.com/youjinChung/BanksyInUs">GitHub Repo</a></strong></em> | <em><strong><a href="https://www.instagram.com/nychristmas2017/">Instagram</a></strong></em><br><em>Featured at ITP Winter Show 2017</em></p>

<iframe src="https://player.vimeo.com/video/285580557" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>

Banksy in us is a project that prints out a holiday theme postcard with a photo image of a user. By face recognition, users are encouraged to make funny faces that match popular gif images. To compare the facial expression, extracted facial points using FaceOSC, and compared the ratio of coordinates.

<div class="side-by-side-images">
<img src="/images/Face-Recognition-Games/-180807_BanksyInUs_UX-Flow.gif" alt="Banksy In Us UX Flow">
<img src="/images/Face-Recognition-Games/ezgif.com-video-to-gif-1.gif" alt="Banksy In Us Demo">
</div>

When the app takes a photo image, users can make a postcard image that looks like Banksy graffitis.

![](images/Face-Recognition-Games/mainImage.jpg)

The final selected postcard image is also printed out as a souvenir, and it can be uploaded to Instagram account if they agree with.

![](images/Face-Recognition-Games/insta01.png)

![](images/Face-Recognition-Games/printed-image.jpg)

## Algorithm

![](images/Face-Recognition-Games/faceRecTable.png)

Sample clips are pre-analyzed with the coordinates of key facial points: Orientation coordinate(x,y,z), Eyebrow heights(left, right), Eye heights(left, right), nose coordinate, mouth width and height. These data are stored in the app, and compared to the user face coordinated to compare the facial expression similarity. The app does not simply compare the coordinates; it compares the ratio of components of the face and the orientation point. This algorithm is devised to deal with different facial structures and the distance from the camera. When the score based on the similarity approaches the threshold, the camera takes a photo of users.

## UX flow

![](images/Face-Recognition-Games/-180807_BanksyInUs_UX-Flow.jpg)

## System

FacsOSC: Face Recognition<br>
Processing: Whole Structure<br>
Webcam: Face image Input<br>
Printer: Postcard Output

## Role

Programming, System Architecture

## Credit

[Namsoo Kim](https://www.vincentnskim.com/): UX design, Documentation

---

# iCeleb

<p style="text-align: right;"><em><strong><a href="https://github.com/youjinChung/iCeleb">GitHub Repo</a></strong></em><br><em>Featured at UCLA Design|Media Arts Solo Show</em></p>

<iframe width="560" height="315" src="https://www.youtube.com/embed/7UtchWMdWG4" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

iCeleb is the prior version of Banksy in Us. It proved the concept of face recognition game. Compared to Banksy In Us which is more like photobooth style interaction/experience, iCeleb accents on game experience that allows players to practice the signature facial expressions of Youtube influencers.

![](images/Face-Recognition-Games/iceleb_short.gif)

<div class="image-carousel-wrapper">
<div class="image-carousel" id="icelebCarousel">
  <div class="carousel-track">
    <img src="/images/Face-Recognition-Games/img_1328_edited.jpg" alt="iCeleb 1">
    <img src="/images/Face-Recognition-Games/p2280081.jpg" alt="iCeleb 2">
    <img src="/images/Face-Recognition-Games/tuangkamol_thongborisute_img_8657.jpg" alt="iCeleb 3">
    <img src="/images/Face-Recognition-Games/tuangkamol_thongborisute_img_8668.jpg" alt="iCeleb 4">
    <img src="/images/Face-Recognition-Games/tuangkamol_thongborisute_img_8674.jpg" alt="iCeleb 5">
  </div>
  <button class="carousel-btn prev" onclick="moveIcelebCarousel(-1)">&lt;</button>
  <button class="carousel-btn next" onclick="moveIcelebCarousel(1)">&gt;</button>
  <div class="carousel-dots"></div>
</div>
</div>

<script>
(function() {
  const carousel = document.getElementById('icelebCarousel');
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

  window.moveIcelebCarousel = function(direction) {
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

  setInterval(() => moveIcelebCarousel(1), 4000);
})();
</script>

## System

FacsOSC: Face Recognition<br>
Processing: Whole Structure<br>
Webcam: Face image Input

## Role

System Architecture, Programming

## Credit

[Tuangkamol Thongborisute](https://tuangstudio.com/): Concept, UX Design, Documentation
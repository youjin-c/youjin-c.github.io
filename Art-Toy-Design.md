---
layout: project
title: Art Toy Design
---

# Final

*October 20, 2018*

## 0. Package Design Update

Printed out the illustrations of the creatures, and laser-cut ear template for display. Meanwhile, wax polished resin stone, so it is more smooth and shiny.  

<div class="image-carousel-wrapper">
<div class="image-carousel" id="packageUpdateCarousel">
  <div class="carousel-track">
    <img src="/images/Art-Toy-Design/u.png" alt="Package Design Update 1">
    <img src="/images/Art-Toy-Design/v.jpeg" alt="Package Design Update 2">
    <img src="/images/Art-Toy-Design/w.jpeg" alt="Package Design Update 3">
    <img src="/images/Art-Toy-Design/q.png" alt="Package Design Update 4">
    <img src="/images/Art-Toy-Design/r.png" alt="Package Design Update 5">
    <img src="/images/Art-Toy-Design/s.png" alt="Package Design Update 6">
    <img src="/images/Art-Toy-Design/t.png" alt="Package Design Update 7">
  </div>
  <button class="carousel-btn prev" onclick="movePackageUpdateCarousel(-1)">&lt;</button>
  <button class="carousel-btn next" onclick="movePackageUpdateCarousel(1)">&gt;</button>
  <div class="carousel-dots"></div>
</div>
</div>

<script>
(function() {
  const carousel = document.getElementById('packageUpdateCarousel');
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

  window.movePackageUpdateCarousel = function(direction) {
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

  setInterval(() => movePackageUpdateCarousel(1), 4000);
})();
</script>

## 1. New creatures

<div class="image-carousel-wrapper">
<div class="image-carousel" id="newCreaturesCarousel">
  <div class="carousel-track">
    <img src="/images/Art-Toy-Design/aa.png" alt="New creatures 1">
    <img src="/images/Art-Toy-Design/x.png" alt="New creatures 2">
    <img src="/images/Art-Toy-Design/y.png" alt="New creatures 3">
    <img src="/images/Art-Toy-Design/z.png" alt="New creatures 4">
  </div>
  <button class="carousel-btn prev" onclick="moveNewCreaturesCarousel(-1)">&lt;</button>
  <button class="carousel-btn next" onclick="moveNewCreaturesCarousel(1)">&gt;</button>
  <div class="carousel-dots"></div>
</div>
</div>

<script>
(function() {
  const carousel = document.getElementById('newCreaturesCarousel');
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
    images.forEach(img => { img.style.width = carouselWidth + 'px'; });
    updateCarousel();
  }

  let loadedCount = 0;
  images.forEach(img => {
    if (img.complete) { loadedCount++; if (loadedCount === totalImages) initCarousel(); }
    else { img.onload = () => { loadedCount++; if (loadedCount === totalImages) initCarousel(); }; }
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

  window.moveNewCreaturesCarousel = function(direction) {
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

  setInterval(() => moveNewCreaturesCarousel(1), 4000);
})();
</script>

Made 3 more shapes in Oculus Medium, tried to make more general fitting earrings that everyone can wear. Inspired by ear hugger, ear jacket shapes and put pin to a piercing so person just can wear like piercings. Printing pin with a toy didn't go well since it was too fragile, I broke all of them while sanding. I switched to drill a hole and put a brass tube into the hole.  

<div class="image-carousel-wrapper">
<div class="image-carousel" id="printingCarousel">
  <div class="carousel-track">
    <img src="/images/Art-Toy-Design/bb.jpeg" alt="Printing 1">
    <img src="/images/Art-Toy-Design/ee.jpeg" alt="Printing 2">
    <img src="/images/Art-Toy-Design/cc.jpeg" alt="Printing 3">
    <img src="/images/Art-Toy-Design/ff.jpeg" alt="Printing 4">
    <img src="/images/Art-Toy-Design/dd.jpeg" alt="Printing 5">
    <img src="/images/Art-Toy-Design/gg.jpeg" alt="Printing 6">
  </div>
  <button class="carousel-btn prev" onclick="movePrintingCarousel(-1)">&lt;</button>
  <button class="carousel-btn next" onclick="movePrintingCarousel(1)">&gt;</button>
  <div class="carousel-dots"></div>
</div>
</div>

<script>
(function() {
  const carousel = document.getElementById('printingCarousel');
  const track = carousel.querySelector('.carousel-track');
  const images = track.querySelectorAll('img');
  const dotsContainer = carousel.querySelector('.carousel-dots');
  let currentIndex = 0;
  const totalImages = images.length;
  let carouselWidth = 0;
  let isAnimating = false;

  function initCarousel() {
    let maxWidth = 0;
    images.forEach(img => { if (img.naturalWidth > maxWidth) maxWidth = img.naturalWidth; });
    carouselWidth = Math.min(maxWidth, carousel.parentElement.offsetWidth);
    carousel.style.width = carouselWidth + 'px';
    images.forEach(img => { img.style.width = carouselWidth + 'px'; });
    updateCarousel();
  }

  let loadedCount = 0;
  images.forEach(img => {
    if (img.complete) { loadedCount++; if (loadedCount === totalImages) initCarousel(); }
    else { img.onload = () => { loadedCount++; if (loadedCount === totalImages) initCarousel(); }; }
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

  window.movePrintingCarousel = function(direction) {
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

  setInterval(() => movePrintingCarousel(1), 4000);
})();
</script>

Printed them, sanded them, and put transparent plastic primer for coloring. I tested water marbling, but the paints are also translucent, turned out too dark.  

<div class="image-carousel-wrapper">
<div class="image-carousel" id="marblingCarousel">
  <div class="carousel-track">
    <img src="/images/Art-Toy-Design/hh.jpeg" alt="Water marbling 1">
    <img src="/images/Art-Toy-Design/jj.jpeg" alt="Water marbling 2">
    <img src="/images/Art-Toy-Design/ii.jpeg" alt="Water marbling 3">
  </div>
  <button class="carousel-btn prev" onclick="moveMarblingCarousel(-1)">&lt;</button>
  <button class="carousel-btn next" onclick="moveMarblingCarousel(1)">&gt;</button>
  <div class="carousel-dots"></div>
</div>
</div>

<script>
(function() {
  const carousel = document.getElementById('marblingCarousel');
  const track = carousel.querySelector('.carousel-track');
  const images = track.querySelectorAll('img');
  const dotsContainer = carousel.querySelector('.carousel-dots');
  let currentIndex = 0;
  const totalImages = images.length;
  let carouselWidth = 0;
  let isAnimating = false;

  function initCarousel() {
    let maxWidth = 0;
    images.forEach(img => { if (img.naturalWidth > maxWidth) maxWidth = img.naturalWidth; });
    carouselWidth = Math.min(maxWidth, carousel.parentElement.offsetWidth);
    carousel.style.width = carouselWidth + 'px';
    images.forEach(img => { img.style.width = carouselWidth + 'px'; });
    updateCarousel();
  }

  let loadedCount = 0;
  images.forEach(img => {
    if (img.complete) { loadedCount++; if (loadedCount === totalImages) initCarousel(); }
    else { img.onload = () => { loadedCount++; if (loadedCount === totalImages) initCarousel(); }; }
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

  window.moveMarblingCarousel = function(direction) {
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

  setInterval(() => moveMarblingCarousel(1), 4000);
})();
</script>

So, sprayed white primer 2-3 times, sanded the surface, water marbled again. The coloring was pretty satisfying / okay to me, but I didn't have time to put vanish on them. I heard the coloring was too dirty during the critique and be recommended to use solid color so people can focus on the shape, rather than the color. I guess I can try to polish them after coloring, it might make people feel better than this sticky feeling, also I definitely try solid colorings. (If I have more time in the future.) Also, the ear film was moving inside of the package, I might try to use vacuum foam of the silicone ear and put them in the box to make it more stable. (Ben + Pedro feedbacks)

<div class="image-carousel-wrapper">
<div class="image-carousel" id="critiqueCarousel">
  <div class="carousel-track">
    <img src="/images/Art-Toy-Design/kk.jpeg" alt="Critique 1">
    <img src="/images/Art-Toy-Design/mm.jpeg" alt="Critique 2">
    <img src="/images/Art-Toy-Design/oo.jpeg" alt="Critique 3">
    <img src="/images/Art-Toy-Design/rr.jpeg" alt="Critique 4">
    <img src="/images/Art-Toy-Design/ll.jpeg" alt="Critique 5">
    <img src="/images/Art-Toy-Design/nn.jpeg" alt="Critique 6">
    <img src="/images/Art-Toy-Design/pp.jpeg" alt="Critique 7">
    <img src="/images/Art-Toy-Design/qq.jpeg" alt="Critique 8">
    <img src="/images/Art-Toy-Design/ss.jpeg" alt="Critique 9">
    <img src="/images/Art-Toy-Design/tt.jpeg" alt="Critique 10">
    <img src="/images/Art-Toy-Design/uu.jpeg" alt="Critique 11">
  </div>
  <button class="carousel-btn prev" onclick="moveCritiqueCarousel(-1)">&lt;</button>
  <button class="carousel-btn next" onclick="moveCritiqueCarousel(1)">&gt;</button>
  <div class="carousel-dots"></div>
</div>
</div>

<script>
(function() {
  const carousel = document.getElementById('critiqueCarousel');
  const track = carousel.querySelector('.carousel-track');
  const images = track.querySelectorAll('img');
  const dotsContainer = carousel.querySelector('.carousel-dots');
  let currentIndex = 0;
  const totalImages = images.length;
  let carouselWidth = 0;
  let isAnimating = false;

  function initCarousel() {
    let maxWidth = 0;
    images.forEach(img => { if (img.naturalWidth > maxWidth) maxWidth = img.naturalWidth; });
    carouselWidth = Math.min(maxWidth, carousel.parentElement.offsetWidth);
    carousel.style.width = carouselWidth + 'px';
    images.forEach(img => { img.style.width = carouselWidth + 'px'; });
    updateCarousel();
  }

  let loadedCount = 0;
  images.forEach(img => {
    if (img.complete) { loadedCount++; if (loadedCount === totalImages) initCarousel(); }
    else { img.onload = () => { loadedCount++; if (loadedCount === totalImages) initCarousel(); }; }
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

  window.moveCritiqueCarousel = function(direction) {
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

  setInterval(() => moveCritiqueCarousel(1), 4000);
})();
</script>

  
  
  


## Package Design

  
0\. Amber making - continued from last week  
  

<div class="image-carousel-wrapper">
<div class="image-carousel" id="amberCarousel">
  <div class="carousel-track">
    <img src="/images/Art-Toy-Design/Screen-Shot-2019-02-14-at-1.18.13-PM.png" alt="Amber making 1">
    <img src="/images/Art-Toy-Design/f.jpeg" alt="Amber making 2">
    <img src="/images/Art-Toy-Design/g.jpeg" alt="Amber making 3">
  </div>
  <button class="carousel-btn prev" onclick="moveAmberCarousel(-1)">&lt;</button>
  <button class="carousel-btn next" onclick="moveAmberCarousel(1)">&gt;</button>
  <div class="carousel-dots"></div>
</div>
</div>

<script>
(function() {
  const carousel = document.getElementById('amberCarousel');
  const track = carousel.querySelector('.carousel-track');
  const images = track.querySelectorAll('img');
  const dotsContainer = carousel.querySelector('.carousel-dots');
  let currentIndex = 0;
  const totalImages = images.length;
  let carouselWidth = 0;
  let isAnimating = false;

  function initCarousel() {
    let maxWidth = 0;
    images.forEach(img => { if (img.naturalWidth > maxWidth) maxWidth = img.naturalWidth; });
    carouselWidth = Math.min(maxWidth, carousel.parentElement.offsetWidth);
    carousel.style.width = carouselWidth + 'px';
    images.forEach(img => { img.style.width = carouselWidth + 'px'; });
    updateCarousel();
  }

  let loadedCount = 0;
  images.forEach(img => {
    if (img.complete) { loadedCount++; if (loadedCount === totalImages) initCarousel(); }
    else { img.onload = () => { loadedCount++; if (loadedCount === totalImages) initCarousel(); }; }
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

  window.moveAmberCarousel = function(direction) {
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

  setInterval(() => moveAmberCarousel(1), 4000);
})();
</script>

Last week I ended up with putting resin in a cup with two Nesi's. They are
totally cured, so I cut them with bandsaw, and sanded. (KA161 ->60 A/0
something ->P320 PB1) As we watched last time, I water sanded with the last
sand paper. I still need to wax polish them. Anyway, I feels so satisfying
like touching a pebble.  

  1. New sketches (including packaging idea)

  
I struggled a lot with Nesi’s curve and scaling, so I changed the approach to
benchmark the structure of ear piercings. There are a lot of attractive
jewelry structure while keeping a simple structure and one size for everyone.
Since I already have Nesi, I will choose three of them.

<div class="image-carousel-wrapper">
<div class="image-carousel" id="jewelryCarousel">
  <div class="carousel-track">
    <img src="/images/Art-Toy-Design/h.jpeg" alt="Jewelry structure 1">
    <img src="/images/Art-Toy-Design/j.jpeg" alt="Jewelry structure 2">
    <img src="/images/Art-Toy-Design/l.jpeg" alt="Jewelry structure 3">
    <img src="/images/Art-Toy-Design/i.jpeg" alt="Jewelry structure 4">
    <img src="/images/Art-Toy-Design/k.jpeg" alt="Jewelry structure 5">
  </div>
  <button class="carousel-btn prev" onclick="moveJewelryCarousel(-1)">&lt;</button>
  <button class="carousel-btn next" onclick="moveJewelryCarousel(1)">&gt;</button>
  <div class="carousel-dots"></div>
</div>
</div>

<script>
(function() {
  const carousel = document.getElementById('jewelryCarousel');
  const track = carousel.querySelector('.carousel-track');
  const images = track.querySelectorAll('img');
  const dotsContainer = carousel.querySelector('.carousel-dots');
  let currentIndex = 0;
  const totalImages = images.length;
  let carouselWidth = 0;
  let isAnimating = false;

  function initCarousel() {
    let maxWidth = 0;
    images.forEach(img => { if (img.naturalWidth > maxWidth) maxWidth = img.naturalWidth; });
    carouselWidth = Math.min(maxWidth, carousel.parentElement.offsetWidth);
    carousel.style.width = carouselWidth + 'px';
    images.forEach(img => { img.style.width = carouselWidth + 'px'; });
    updateCarousel();
  }

  let loadedCount = 0;
  images.forEach(img => {
    if (img.complete) { loadedCount++; if (loadedCount === totalImages) initCarousel(); }
    else { img.onload = () => { loadedCount++; if (loadedCount === totalImages) initCarousel(); }; }
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

  window.moveJewelryCarousel = function(direction) {
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

  setInterval(() => moveJewelryCarousel(1), 4000);
})();
</script>

For package design, I was inspired by vacuum tubes. I ordered plastic tube and
caps from Uline (I don’t need 25 sets of them though…). What I need to do is
laser cut cardboards to ear shape and pin my jewelry toy on the cardboard, and
hang them tight in the cylinder. So I can display them in the package and give
audience a sense of how to wear them. I wish I can draw some art-toy like
label.

<div class="image-carousel-wrapper">
<div class="image-carousel" id="tubesCarousel">
  <div class="carousel-track">
    <img src="/images/Art-Toy-Design/o.jpeg" alt="Package tubes 1">
    <img src="/images/Art-Toy-Design/p.jpeg" alt="Package tubes 2">
    <img src="/images/Art-Toy-Design/output.gif" alt="Package tubes 3">
  </div>
  <button class="carousel-btn prev" onclick="moveTubesCarousel(-1)">&lt;</button>
  <button class="carousel-btn next" onclick="moveTubesCarousel(1)">&gt;</button>
  <div class="carousel-dots"></div>
</div>
</div>

<script>
(function() {
  const carousel = document.getElementById('tubesCarousel');
  const track = carousel.querySelector('.carousel-track');
  const images = track.querySelectorAll('img');
  const dotsContainer = carousel.querySelector('.carousel-dots');
  let currentIndex = 0;
  const totalImages = images.length;
  let carouselWidth = 0;
  let isAnimating = false;

  function initCarousel() {
    let maxWidth = 0;
    images.forEach(img => { if (img.naturalWidth > maxWidth) maxWidth = img.naturalWidth; });
    carouselWidth = Math.min(maxWidth, carousel.parentElement.offsetWidth);
    carousel.style.width = carouselWidth + 'px';
    images.forEach(img => { img.style.width = carouselWidth + 'px'; });
    updateCarousel();
  }

  let loadedCount = 0;
  images.forEach(img => {
    if (img.complete) { loadedCount++; if (loadedCount === totalImages) initCarousel(); }
    else { img.onload = () => { loadedCount++; if (loadedCount === totalImages) initCarousel(); }; }
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

  window.moveTubesCarousel = function(direction) {
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

  setInterval(() => moveTubesCarousel(1), 4000);
})();
</script>

cut the rods from Nesi.  


## Finish

I learned a lot this week, means epic failed again and again.  
  
Since Saturday I 3d printed lots of time, and even silicone molded with the
model.

![](/images/Art-Toy-Design/Screen-Shot-2019-02-14-at-1.14.17-PM.png)

  * The size: 32-35mm is fitting for general ear sizes. But I cannot sell these as earrings online since all ears are so different, unless I find a magical way to measure people's ear remotely. When I use Cura, it was around 35% scale of the original 3d object file.

![](/images/Art-Toy-Design/Screen-Shot-2019-02-14-at-1.14.25-PM.png)

Watch tutorial before use the material..!!!! I didn’t and learned by
experience, which was totally preventable. I used Smooth on Dragon Skin and
Crystal Clear 202 and they have terrific video tutorial for “Resin mold for 3d
printed model”….Anyways, what I learned were  

  * I need TWO tunnel for resin mold if I want to pour resin through the silicone cast. That was the main reason I 3d printed the model again.
  * It's hard to glue rod on PLA printed model… It's much better to print all of them from beginning.

<div class="image-carousel-wrapper">
<div class="image-carousel" id="tunnelCarousel">
  <div class="carousel-track">
    <img src="/images/Art-Toy-Design/A.jpeg" alt="Tunnel 1">
    <img src="/images/Art-Toy-Design/B.jpeg" alt="Tunnel 2">
    <img src="/images/Art-Toy-Design/C.jpeg" alt="Tunnel 3">
    <img src="/images/Art-Toy-Design/D.jpeg" alt="Tunnel 4">
  </div>
  <button class="carousel-btn prev" onclick="moveTunnelCarousel(-1)">&lt;</button>
  <button class="carousel-btn next" onclick="moveTunnelCarousel(1)">&gt;</button>
  <div class="carousel-dots"></div>
</div>
</div>

<script>
(function() {
  const carousel = document.getElementById('tunnelCarousel');
  const track = carousel.querySelector('.carousel-track');
  const images = track.querySelectorAll('img');
  const dotsContainer = carousel.querySelector('.carousel-dots');
  let currentIndex = 0;
  const totalImages = images.length;
  let carouselWidth = 0;
  let isAnimating = false;

  function initCarousel() {
    let maxWidth = 0;
    images.forEach(img => { if (img.naturalWidth > maxWidth) maxWidth = img.naturalWidth; });
    carouselWidth = Math.min(maxWidth, carousel.parentElement.offsetWidth);
    carousel.style.width = carouselWidth + 'px';
    images.forEach(img => { img.style.width = carouselWidth + 'px'; });
    updateCarousel();
  }

  let loadedCount = 0;
  images.forEach(img => {
    if (img.complete) { loadedCount++; if (loadedCount === totalImages) initCarousel(); }
    else { img.onload = () => { loadedCount++; if (loadedCount === totalImages) initCarousel(); }; }
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

  window.moveTunnelCarousel = function(direction) {
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

  setInterval(() => moveTunnelCarousel(1), 4000);
})();
</script>

I sanded with 0. coarse sand paper 1. nail filer 2. fine sandpaper and the
last one felt like stone. It was so good but I kept breaking legs for each
model. It was frustrating and consuming a lot of time, and I noticed,  

  * Who decided Nesi has four legs? It is so boring having four legs. It could be odd number, too many or even none! legs are not even supposed to seem like regular legs.
  * Having these tiny legs is definitely wrong design for 3d prototyping.

  
I decided go with 2 legs left after sanding.

![](/images/Art-Toy-Design/Screen-Shot-2019-02-14-at-1.15.04-PM.png)

Nesi with 2 legs looked awesome, it seems a bit of a plant and an animal at
the same time.

![](/images/Art-Toy-Design/Screen-Shot-2019-02-14-at-1.15.27-PM.png)

I went through silicone casting and resin mold with a new model and found I am
wasting material compare to the size of my model..I need to find a way to save
them. I just put a blue color for the first trial, but I will try color mix if
the resin mold success. With the resin leftover, I made preserved Nesi’s.
(Hopefully they could look like amber fossils.)  


## MATERIAL AND TECHNIQUE SCULPT

This week I just went through the whole process to the finish of my sculpture.  
  
Bottom line first, I decided to use resin mold for rest of this semester.
Considering the shape of my toy, I cannot use CNC unless break down the
sculpture.  
If I stick with 3D printing, there are 3 ways to do that:  
-PLA(most common) print and do after works.  
-Resin printing  
-PLA prototype and resin molding  
  
The merits of resin mold are coloring and preciseness. I tried to color and
polish the 3D model this week, and it just revealed how bad I am with
painting, also even sanding. If I want to color the PLA printed model, I’d
better use spray brushes. but I still need to make maskings for color blocks.  
  
Resin mold is a traditional technique for high-end jewelries and fountain
pens, which makes my toy more persuasive as a product.

![](/images/Art-Toy-Design/000.png)

![](/images/Art-Toy-Design/111.png)

I got some inspiration meanwhile

  * sneakers color blocking - I was thinking art/designer toys are alike sneakers somehow. Since the streetwear culture is what I am familiar with than art toy, I wanted to co-op them.

<div class="image-carousel-wrapper">
<div class="image-carousel" id="sneakersCarousel">
  <div class="carousel-track">
    <img src="/images/Art-Toy-Design/222.png" alt="Sneakers 1">
    <img src="/images/Art-Toy-Design/333.png" alt="Sneakers 2">
    <img src="/images/Art-Toy-Design/444.png" alt="Sneakers 3">
  </div>
  <button class="carousel-btn prev" onclick="moveSneakersCarousel(-1)">&lt;</button>
  <button class="carousel-btn next" onclick="moveSneakersCarousel(1)">&gt;</button>
  <div class="carousel-dots"></div>
</div>
</div>

<script>
(function() {
  const carousel = document.getElementById('sneakersCarousel');
  const track = carousel.querySelector('.carousel-track');
  const images = track.querySelectorAll('img');
  const dotsContainer = carousel.querySelector('.carousel-dots');
  let currentIndex = 0;
  const totalImages = images.length;
  let carouselWidth = 0;
  let isAnimating = false;

  function initCarousel() {
    let maxWidth = 0;
    images.forEach(img => { if (img.naturalWidth > maxWidth) maxWidth = img.naturalWidth; });
    carouselWidth = Math.min(maxWidth, carousel.parentElement.offsetWidth);
    carousel.style.width = carouselWidth + 'px';
    images.forEach(img => { img.style.width = carouselWidth + 'px'; });
    updateCarousel();
  }

  let loadedCount = 0;
  images.forEach(img => {
    if (img.complete) { loadedCount++; if (loadedCount === totalImages) initCarousel(); }
    else { img.onload = () => { loadedCount++; if (loadedCount === totalImages) initCarousel(); }; }
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

  window.moveSneakersCarousel = function(direction) {
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

  setInterval(() => moveSneakersCarousel(1), 4000);
})();
</script>

  * glossy finish - the candy-like, glossy and smooth finish caught me. Especially ceramic glaze finish looked so cool to me.

![](/images/Art-Toy-Design/555.png)

![](/images/Art-Toy-Design/666.png)

  * wearable - my toys will be wearable anyway, I need to exchange some part of toy with metal. Many earrings such as ear hoop, ear climbers, ear jackets are actually bendable so customers can adjust jewelry to their body. I think I can print bass part when I decide the final 3d model.

  
The plan for the final 4 pieces are like this.  

  1. The original color-blocking ear bug.
  2. one with fur on the belly.
  3. one with audio filter by DIY PCB. Neuromancer inspired.
  4. chimera version with bone / insect crust.

  
For actual scaling, I made a clay version of the creature and measured it. It
was 37.53mm from end to end, I can scale 3d model again for prototype.

<div class="image-carousel-wrapper">
<div class="image-carousel" id="clayCarousel">
  <div class="carousel-track">
    <img src="/images/Art-Toy-Design/777.jpeg" alt="Clay scaling 1">
    <img src="/images/Art-Toy-Design/888.jpeg" alt="Clay scaling 2">
    <img src="/images/Art-Toy-Design/999.jpeg" alt="Clay scaling 3">
    <img src="/images/Art-Toy-Design/1010.jpeg" alt="Clay scaling 4">
    <img src="/images/Art-Toy-Design/1212.jpeg" alt="Clay scaling 5">
    <img src="/images/Art-Toy-Design/1111.jpeg" alt="Clay scaling 6">
    <img src="/images/Art-Toy-Design/1313.jpeg" alt="Clay scaling 7">
  </div>
  <button class="carousel-btn prev" onclick="moveClayCarousel(-1)">&lt;</button>
  <button class="carousel-btn next" onclick="moveClayCarousel(1)">&gt;</button>
  <div class="carousel-dots"></div>
</div>
</div>

<script>
(function() {
  const carousel = document.getElementById('clayCarousel');
  const track = carousel.querySelector('.carousel-track');
  const images = track.querySelectorAll('img');
  const dotsContainer = carousel.querySelector('.carousel-dots');
  let currentIndex = 0;
  const totalImages = images.length;
  let carouselWidth = 0;
  let isAnimating = false;

  function initCarousel() {
    let maxWidth = 0;
    images.forEach(img => { if (img.naturalWidth > maxWidth) maxWidth = img.naturalWidth; });
    carouselWidth = Math.min(maxWidth, carousel.parentElement.offsetWidth);
    carousel.style.width = carouselWidth + 'px';
    images.forEach(img => { img.style.width = carouselWidth + 'px'; });
    updateCarousel();
  }

  let loadedCount = 0;
  images.forEach(img => {
    if (img.complete) { loadedCount++; if (loadedCount === totalImages) initCarousel(); }
    else { img.onload = () => { loadedCount++; if (loadedCount === totalImages) initCarousel(); }; }
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

  window.moveClayCarousel = function(direction) {
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

  setInterval(() => moveClayCarousel(1), 4000);
})();
</script>

I sanded it and sprayed the primer. I broke a leg and the tail tip while
sanding. Maybe I can try tumbler in stead of sanding. I heard I can wipe with
alcohol if I want to color 3d printed models. (Before using primer I guess) I
can try next time.  

  
I marked borderline with sharpie. I expected the facial expression remains,
but the sharpie blurred and disappeared when I painted only one time. A very
basic tip - paint with bright color first..

<div class="image-carousel-wrapper">
<div class="image-carousel" id="sharpieCarousel">
  <div class="carousel-track">
    <img src="/images/Art-Toy-Design/1414.jpeg" alt="Sharpie 1">
    <img src="/images/Art-Toy-Design/1515.jpeg" alt="Sharpie 2">
    <img src="/images/Art-Toy-Design/1616.jpeg" alt="Sharpie 3">
    <img src="/images/Art-Toy-Design/1717.jpeg" alt="Sharpie 4">
  </div>
  <button class="carousel-btn prev" onclick="moveSharpieCarousel(-1)">&lt;</button>
  <button class="carousel-btn next" onclick="moveSharpieCarousel(1)">&gt;</button>
  <div class="carousel-dots"></div>
</div>
</div>

<script>
(function() {
  const carousel = document.getElementById('sharpieCarousel');
  const track = carousel.querySelector('.carousel-track');
  const images = track.querySelectorAll('img');
  const dotsContainer = carousel.querySelector('.carousel-dots');
  let currentIndex = 0;
  const totalImages = images.length;
  let carouselWidth = 0;
  let isAnimating = false;

  function initCarousel() {
    let maxWidth = 0;
    images.forEach(img => { if (img.naturalWidth > maxWidth) maxWidth = img.naturalWidth; });
    carouselWidth = Math.min(maxWidth, carousel.parentElement.offsetWidth);
    carousel.style.width = carouselWidth + 'px';
    images.forEach(img => { img.style.width = carouselWidth + 'px'; });
    updateCarousel();
  }

  let loadedCount = 0;
  images.forEach(img => {
    if (img.complete) { loadedCount++; if (loadedCount === totalImages) initCarousel(); }
    else { img.onload = () => { loadedCount++; if (loadedCount === totalImages) initCarousel(); }; }
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

  window.moveSharpieCarousel = function(direction) {
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

  setInterval(() => moveSharpieCarousel(1), 4000);
})();
</script>

Anyways, finished with glossy vanish and waiting to dry.. One thing to think
about is, how to express color block while using resin mold.  


## SCULPT YOUR TOY

My goal of this class is making wearable art toys, especially on ears.

![](/images/Art-Toy-Design/00.jpeg)

Bought some silicon ear model from Amazon. It’s hard to borrow someone’s ear
all the time, these are for hands on fabrication and scaling.  
  
I bought some clay and wires for sculpting anyway, I tried Oculus Medium and
it was much intuitive and easy than I expect. I just finished my first piece.

![](/images/Art-Toy-Design/11.png)

I used an ear stamp as base, and put continuous clay over it. Since I used 2
separate layers, there’s no issue for extraction or so on. After putting
clays, I turned off the layer of the ear stamp so the size and coordinate is
off. Mostly I used smoothing tool, cuz swirl made clay twist in clockwise.

![](/images/Art-Toy-Design/22.png)

I was inspired Nesi laying on back on the surface of the ear. Wanted to put
furry fair on the belly later. I can still try when I find the right scale.  
  
All the earring series will be inspired on fears regarding ears, such as
water, ear bugs, optic nerve coming from earring holes…(totally urban legend)

![](/images/Art-Toy-Design/33.jpg)

Medium was super intuitive though, the big pitfall is hard to scale to real
size. 3D modeling tools provide measures thought, it won’t be accurate till I
make a real size prototype and measure equivalent points.

![](/images/Art-Toy-Design/44.jpeg)

![](/images/Art-Toy-Design/55.jpeg)

Apparently too small for ears, but I guess you can get the sense what I
intended.  
I scaled up the model with meshlab. (it’s the most reachable tool for me) I
scaled twice for each axis, meaning 8 times inflated than the original. (and I
was a mistake. should done root 2 times scaling.) but the good part was I
figured out that VR modeling is too low poly and I could to Laplacian
smoothing with MeshLab.

![](/images/Art-Toy-Design/66.png)

I even put eyeballs on it, but it was not distinguishable for its size. I
scaled it up 8 times bigger and printed again. The thing is I need to make a
file using Ultimaker Cura or Cura Lulzbot edition and it was such pain in the
ass. Both didn't running well on MacOS.

<div class="image-carousel-wrapper">
<div class="image-carousel" id="eyeballsCarousel">
  <div class="carousel-track">
    <img src="/images/Art-Toy-Design/77.jpeg" alt="Eyeballs 1">
    <img src="/images/Art-Toy-Design/88.jpeg" alt="Eyeballs 2">
    <img src="/images/Art-Toy-Design/99.jpeg" alt="Eyeballs 3">
  </div>
  <button class="carousel-btn prev" onclick="moveEyeballsCarousel(-1)">&lt;</button>
  <button class="carousel-btn next" onclick="moveEyeballsCarousel(1)">&gt;</button>
  <div class="carousel-dots"></div>
</div>
</div>

<script>
(function() {
  const carousel = document.getElementById('eyeballsCarousel');
  const track = carousel.querySelector('.carousel-track');
  const images = track.querySelectorAll('img');
  const dotsContainer = carousel.querySelector('.carousel-dots');
  let currentIndex = 0;
  const totalImages = images.length;
  let carouselWidth = 0;
  let isAnimating = false;

  function initCarousel() {
    let maxWidth = 0;
    images.forEach(img => { if (img.naturalWidth > maxWidth) maxWidth = img.naturalWidth; });
    carouselWidth = Math.min(maxWidth, carousel.parentElement.offsetWidth);
    carousel.style.width = carouselWidth + 'px';
    images.forEach(img => { img.style.width = carouselWidth + 'px'; });
    updateCarousel();
  }

  let loadedCount = 0;
  images.forEach(img => {
    if (img.complete) { loadedCount++; if (loadedCount === totalImages) initCarousel(); }
    else { img.onload = () => { loadedCount++; if (loadedCount === totalImages) initCarousel(); }; }
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

  window.moveEyeballsCarousel = function(direction) {
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

  setInterval(() => moveEyeballsCarousel(1), 4000);
})();
</script>

The second one was too big. I can still go for the finishing, such as using
spray brush or resin coating, and putting hair on the belly! I also learned
removing supports is hard in the case of organic shape. I need swirl for this.  


## BLANK MODIFICATION

  
We’ve got 3 wooden pegs to modify.  
  
Searched junk shelf, and got some junk pieces and inspiration.  
putting a wheel.  
I found a wheel for chair. I put a hole on the bottom of the peg to hammer the
wheel inside.

![](/images/Art-Toy-Design/0.jpeg)

![](/images/Art-Toy-Design/1.jpeg)

It seemed a bit simple, so I made a hat for it.

![](/images/Art-Toy-Design/2.jpeg)

![](/images/Art-Toy-Design/3.jpeg)

  

  * Switch a head with an eyeball  
  
Interestingly, Phil found an eyeball on the floor that looks like one in my
character drawing. Inspired by Sauron, I made a… Sauron peg.

![](/images/Art-Toy-Design/5.jpeg)

Simply I cut the head of the peg with a bandsaw, and put a plastic eyeball
with glue.

![](/images/Art-Toy-Design/6.jpeg)

I had mylar sheet in my bin, made a cloak for it.

<div class="image-carousel-wrapper">
<div class="image-carousel" id="cloakCarousel">
  <div class="carousel-track">
    <img src="/images/Art-Toy-Design/7.jpeg" alt="Cloak 1">
    <img src="/images/Art-Toy-Design/8.jpeg" alt="Cloak 2">
    <img src="/images/Art-Toy-Design/9.jpeg" alt="Cloak 3">
  </div>
  <button class="carousel-btn prev" onclick="moveCloakCarousel(-1)">&lt;</button>
  <button class="carousel-btn next" onclick="moveCloakCarousel(1)">&gt;</button>
  <div class="carousel-dots"></div>
</div>
</div>

<script>
(function() {
  const carousel = document.getElementById('cloakCarousel');
  const track = carousel.querySelector('.carousel-track');
  const images = track.querySelectorAll('img');
  const dotsContainer = carousel.querySelector('.carousel-dots');
  let currentIndex = 0;
  const totalImages = images.length;
  let carouselWidth = 0;
  let isAnimating = false;

  function initCarousel() {
    let maxWidth = 0;
    images.forEach(img => { if (img.naturalWidth > maxWidth) maxWidth = img.naturalWidth; });
    carouselWidth = Math.min(maxWidth, carousel.parentElement.offsetWidth);
    carousel.style.width = carouselWidth + 'px';
    images.forEach(img => { img.style.width = carouselWidth + 'px'; });
    updateCarousel();
  }

  let loadedCount = 0;
  images.forEach(img => {
    if (img.complete) { loadedCount++; if (loadedCount === totalImages) initCarousel(); }
    else { img.onload = () => { loadedCount++; if (loadedCount === totalImages) initCarousel(); }; }
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

  window.moveCloakCarousel = function(direction) {
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

  setInterval(() => moveCloakCarousel(1), 4000);
})();
</script>

  * Cut in a half

  
I make a hole and cut a head, why not cutting in half?

![](/images/Art-Toy-Design/10.jpeg)

So just did it. Originally wanted to draw intestines on the surface but was
recommended dig the flat surface and put some thread or yarn to add texture to
the peg. (Also it is easier than drawing.)

![](/images/Art-Toy-Design/11.jpeg)

I tried to dig the surface. I didn't have gravers but we had drop-drill(don't
remember the name). I needed to tie the halves with a rubber band and make a
hole between them. I should have drilled a hole first and cut in half later.

![](/images/Art-Toy-Design/12.jpeg)

I had a acrylic mirror sheet. My plan was to let people see the intestines
through the mirror. I measured the size of the peg, and cut the acrylic with
bandsaw, and sanded to curves.

<div class="image-carousel-wrapper">
<div class="image-carousel" id="mirrorCarousel">
  <div class="carousel-track">
    <img src="/images/Art-Toy-Design/13.jpeg" alt="Mirror 1">
    <img src="/images/Art-Toy-Design/14.jpeg" alt="Mirror 2">
    <img src="/images/Art-Toy-Design/15.jpeg" alt="Mirror 3">
    <img src="/images/Art-Toy-Design/16.jpeg" alt="Mirror 4">
  </div>
  <button class="carousel-btn prev" onclick="moveMirrorCarousel(-1)">&lt;</button>
  <button class="carousel-btn next" onclick="moveMirrorCarousel(1)">&gt;</button>
  <div class="carousel-dots"></div>
</div>
</div>

<script>
(function() {
  const carousel = document.getElementById('mirrorCarousel');
  const track = carousel.querySelector('.carousel-track');
  const images = track.querySelectorAll('img');
  const dotsContainer = carousel.querySelector('.carousel-dots');
  let currentIndex = 0;
  const totalImages = images.length;
  let carouselWidth = 0;
  let isAnimating = false;

  function initCarousel() {
    let maxWidth = 0;
    images.forEach(img => { if (img.naturalWidth > maxWidth) maxWidth = img.naturalWidth; });
    carouselWidth = Math.min(maxWidth, carousel.parentElement.offsetWidth);
    carousel.style.width = carouselWidth + 'px';
    images.forEach(img => { img.style.width = carouselWidth + 'px'; });
    updateCarousel();
  }

  let loadedCount = 0;
  images.forEach(img => {
    if (img.complete) { loadedCount++; if (loadedCount === totalImages) initCarousel(); }
    else { img.onload = () => { loadedCount++; if (loadedCount === totalImages) initCarousel(); }; }
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

  window.moveMirrorCarousel = function(direction) {
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

  setInterval(() => moveMirrorCarousel(1), 4000);
})();
</script>

Lastly, found yarns and wires and glues in the gut of the peg. I finished the
toy by putting mirrors and the peg on the piece of wood.

<div class="image-carousel-wrapper">
<div class="image-carousel" id="finalPegCarousel">
  <div class="carousel-track">
    <img src="/images/Art-Toy-Design/17.jpeg" alt="Final peg 1">
    <img src="/images/Art-Toy-Design/18.jpeg" alt="Final peg 2">
    <img src="/images/Art-Toy-Design/19.jpeg" alt="Final peg 3">
    <img src="/images/Art-Toy-Design/20.jpeg" alt="Final peg 4">
  </div>
  <button class="carousel-btn prev" onclick="moveFinalPegCarousel(-1)">&lt;</button>
  <button class="carousel-btn next" onclick="moveFinalPegCarousel(1)">&gt;</button>
  <div class="carousel-dots"></div>
</div>
</div>

<script>
(function() {
  const carousel = document.getElementById('finalPegCarousel');
  const track = carousel.querySelector('.carousel-track');
  const images = track.querySelectorAll('img');
  const dotsContainer = carousel.querySelector('.carousel-dots');
  let currentIndex = 0;
  const totalImages = images.length;
  let carouselWidth = 0;
  let isAnimating = false;

  function initCarousel() {
    let maxWidth = 0;
    images.forEach(img => { if (img.naturalWidth > maxWidth) maxWidth = img.naturalWidth; });
    carouselWidth = Math.min(maxWidth, carousel.parentElement.offsetWidth);
    carousel.style.width = carouselWidth + 'px';
    images.forEach(img => { img.style.width = carouselWidth + 'px'; });
    updateCarousel();
  }

  let loadedCount = 0;
  images.forEach(img => {
    if (img.complete) { loadedCount++; if (loadedCount === totalImages) initCarousel(); }
    else { img.onload = () => { loadedCount++; if (loadedCount === totalImages) initCarousel(); }; }
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

  window.moveFinalPegCarousel = function(direction) {
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

  setInterval(() => moveFinalPegCarousel(1), 4000);
})();
</script>


## Character Turnarounds

<div class="image-carousel-wrapper">
<div class="image-carousel" id="turnaroundsCarousel">
  <div class="carousel-track">
    <img src="/images/Art-Toy-Design/ct0.jpeg" alt="Turnarounds 1">
    <img src="/images/Art-Toy-Design/ct1.jpeg" alt="Turnarounds 2">
    <img src="/images/Art-Toy-Design/ct2.jpeg" alt="Turnarounds 3">
  </div>
  <button class="carousel-btn prev" onclick="moveTurnaroundsCarousel(-1)">&lt;</button>
  <button class="carousel-btn next" onclick="moveTurnaroundsCarousel(1)">&gt;</button>
  <div class="carousel-dots"></div>
</div>
</div>

<script>
(function() {
  const carousel = document.getElementById('turnaroundsCarousel');
  const track = carousel.querySelector('.carousel-track');
  const images = track.querySelectorAll('img');
  const dotsContainer = carousel.querySelector('.carousel-dots');
  let currentIndex = 0;
  const totalImages = images.length;
  let carouselWidth = 0;
  let isAnimating = false;

  function initCarousel() {
    let maxWidth = 0;
    images.forEach(img => { if (img.naturalWidth > maxWidth) maxWidth = img.naturalWidth; });
    carouselWidth = Math.min(maxWidth, carousel.parentElement.offsetWidth);
    carousel.style.width = carouselWidth + 'px';
    images.forEach(img => { img.style.width = carouselWidth + 'px'; });
    updateCarousel();
  }

  let loadedCount = 0;
  images.forEach(img => {
    if (img.complete) { loadedCount++; if (loadedCount === totalImages) initCarousel(); }
    else { img.onload = () => { loadedCount++; if (loadedCount === totalImages) initCarousel(); }; }
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

  window.moveTurnaroundsCarousel = function(direction) {
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

  setInterval(() => moveTurnaroundsCarousel(1), 4000);
})();
</script>

On the first day, we did intense character drawing. I chose tooth + slime
theme, and got couple of drafts.  
  
Based on them, I come up with a wisdom teeth character and drew a turnaround
of it.

![](/images/Art-Toy-Design/3.jpg)
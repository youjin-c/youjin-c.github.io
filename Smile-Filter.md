---
layout: project
title: Smile Filter
---

<div class="image-carousel-wrapper">
<div class="image-carousel" id="smileCarousel">
  <div class="carousel-track">
    <img src="/images/Smile-Filter/two_image_side0.jpg" alt="Smile Filter example 1">
    <img src="/images/Smile-Filter/two_image_side1.jpg" alt="Smile Filter example 2">
    <img src="/images/Smile-Filter/two_image_side2.jpg" alt="Smile Filter example 3">
    <img src="/images/Smile-Filter/two_image_side3.jpg" alt="Smile Filter example 4">
    <img src="/images/Smile-Filter/two_image_side4.jpg" alt="Smile Filter example 5">
    <img src="/images/Smile-Filter/two_image_side5.jpg" alt="Smile Filter example 6">
    <img src="/images/Smile-Filter/two_image_side6.jpg" alt="Smile Filter example 7">
  </div>
  <button class="carousel-btn prev" onclick="moveCarousel(-1)">&lt;</button>
  <button class="carousel-btn next" onclick="moveCarousel(1)">&gt;</button>
  <div class="carousel-dots"></div>
</div>
</div>

<script>
(function() {
  const carousel = document.getElementById('smileCarousel');
  const track = carousel.querySelector('.carousel-track');
  const images = track.querySelectorAll('img');
  const dotsContainer = carousel.querySelector('.carousel-dots');
  let currentIndex = 0;
  const totalImages = images.length;
  let carouselWidth = 0;

  // Wait for first image to load to set fixed dimensions
  images[0].onload = function() {
    carouselWidth = this.naturalWidth;
    carousel.style.width = carouselWidth + 'px';
    images.forEach(img => {
      img.style.width = carouselWidth + 'px';
    });
  };

  // Create dots
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

  window.moveCarousel = function(direction) {
    currentIndex = (currentIndex + direction + totalImages) % totalImages;
    updateCarousel();
  };

  function goToSlide(index) {
    currentIndex = index;
    updateCarousel();
  }

  // Auto-advance every 4 seconds
  setInterval(() => moveCarousel(1), 4000);
})();
</script>

left: input, right: output

Welcome to my Smile Filter project, where I utilized CycleGAN to transform
facial expressions from normal or unhappy faces to happy faces with mouth
expressions. This project aims to demonstrate the power of image-to-image
translation using unpaired datasets and how it can be applied to improve the
emotional expressions in images.

## CycleGAN

![](images/Smile-Filter/cycleGAN.gif)

CycleGAN is an effective deep learning model for image-to-image translation
with unpaired datasets. It works best when the input and output have similar
geometric constructions, such as apple-orange or horse-zebra. For this
project, I utilized CycleGAN to transform normal or unhappy facial expressions
to happy expressions with mouth expressions.

## Dataset

![](images/Smile-Filter/ffhq-teaser.png)

To train the CycleGAN model, I used the Flickr-Faces-HQ Dataset (FFHQ), a
high-resolution dataset containing 5055 images with a resolution of 256 x 256
pixels. I categorized the images into two groups based on their facial
expressions: normal or unhappy faces and happy faces with mouth expressions.

## Training

The training of the model was performed on AWS EC2 p3.8xlarge, which is
equipped with four Tesla V100s of 64GB GPU memory. I used the Compression And
Teaching (CAT) framework in PyTorch for training the teacher models. Then, I
employed GAN compression to reduce the size of the model, enhance the frame
rate, and reduce the computational cost. Finally, I exported the model into
ONNX format.

## Running model on mobile

![](images/Smile-Filter/teaser.png)

The GAN compressed model can be easily deployed on mobile devices, enabling
real-time facial expression transformations. This provides a seamless user
experience and makes it easier to integrate the model into various
applications.

## Conclusion

In summary, my Smile Filter project demonstrates the power of CycleGAN for
image-to-image translation and how it can be utilized to improve facial
expressions in images. The use of GAN compression reduces the size of the
model, making it suitable for deployment on mobile devices. I hope this
project inspires further research and applications in the field of computer
vision.

## Reference

[NVlabs - Flickr-Faces-HQ Dataset (FFHQ)](https://github.com/NVlabs/ffhq-dataset)

[Compression And Teaching (CAT)](https://github.com/snap-research/CAT)

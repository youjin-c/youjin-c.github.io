---
layout: project
title: Blow A Kiss
---

## Video

<iframe src="https://player.vimeo.com/video/678667262" allowfullscreen></iframe>

## Instruction

1\. Open your mouth to blow a kiss!  
2\. Target the heart to spin it faster!  
3\. Wink to change the color of the heart!

## Process

### Idea

I had an initial idea to make an AR effect that users can interact with the environment object with the user's interaction input. Most users hold a phone while playing AR apps. So I avoided touch input, using the most accessible interaction inputs, opening mouth, and closing eyes.

<img src="images/Blow-A-Kiss/Untitled_Artwork.png" style="width: 70%;">

Once I decided on facial expressions for interaction, I could come up with the idea of kiss and wink. The idea moved to the 'Face Blowing a Kiss 😘' emoji and the look and feel of the AR effect. On top of that, it would go along with the romantic effects of Valentine's day.

### Structure

Unity provides complete access to components of the development, compared to Spark AR or Lens Studio. Even though Spark AR and Lens Studio provide better features focusing on AR effects development, they aim at patch/block-based development. That limits control over elements while programming. I found that Unity MARS can also provide essential features for AR effect making, such as face landmark tracking and facial expression events. So decided to work on Unity MARS for the project.

![](images/Blow-A-Kiss/BlowAKiss.png)

## Trial & Errors

### AR Face Mask
I made a reflective mask on the detected facial mesh. I intended to show the light change on the face according to the interaction input. It worked with existing project dependency and setting. However, the facial mesh edge was too distinctive compared to other commercial AR filters; you can see the border of the forehead and chin. I decided not to include this effect in this project.

<img src="images/Blow-A-Kiss/IMG_4666.jpg" style="width: 60%;">

### Reflection Probe in AR
I tried to include reflection probes for a more realistic visual effect in the scene. However, the AR reflection probe only worked with the rear camera. I could not adopt it for the front user camera scenario.

![](images/Blow-A-Kiss/base64_0_779f8e62.png)

## Further Steps

New interaction input for world AR scenario.<br>
I'd like to try body pose input, location of people, GPS, and landmark anchoring.

## Assets Credit

[Cartoon Kiss_cjohnstone.wav, trijohnstone, Freesound](https://freesound.org/people/trijohnstone/sounds/536335/)<br>
[Heart Symbol Low Poly Free low-poly 3D model, VARRRG, Cgtrader](https://www.cgtrader.com/free-3d-models/character/anatomy/love-low-poly)<br>
[3D model heart, honyzirbu, Turbosquid](https://www.turbosquid.com/3d-models/3d-model-heart-shape-1596418)
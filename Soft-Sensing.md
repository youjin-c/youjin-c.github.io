---
layout: project
title: Soft Sensing
---

# Beautiful sensor: Go Card

*October 8, 2018*

For the last soft sensing project, we decided to focus on one material - conductive paint. We are inspired by a circuit book using conductive tape and paint during the class, decided to make a Korean education kit.

Hangul, Korean letter has an unique system, the letters are assembled to make a sound. If we use a conductive paint, we can stack each sound/letter card on each other.

![](/images/Soft-Sensing/1.jpg)

We chose "ㄱ" + "ㅏ" = "가", 가 is the most simple and basic letter when you learn Korean as we learn A,B,C in English. 가 also has meaning of 'Go', so we named our kit as Go Card.

![](/images/Soft-Sensing/2.jpg)

Even though conductive paint is rather conductive (as the name says) than resistive, the stroke to draw each letter is different. We can make parallel resistance by stacking cards on the kit, and what we need to do is just play sound. We adjusted the last Angry bird returns code.

Laser cut acrylic board for our card and Arduino spacing.

![](/images/Soft-Sensing/3.jpeg)

After we painted conductive paint, and soldered the analog read circuit on the perf board.

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/294069607?h=&title=0&byline=0&portrait=0" style="position:absolute;top:0;left:0;width:100%;height:100%;" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe></div>

<br>

Since the paint is not super durable, but it was good enough to see our concept works. In the same way, we can extend to different Hangul letters.

<br>

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/294069117?h=&title=0&byline=0&portrait=0" style="position:absolute;top:0;left:0;width:100%;height:100%;" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe></div>

---

# Research group: Angry Bird Returns

*October 8, 2018*

On the second day, we focused on stretch fabric and come up with the idea of making a slingshot for angry birds. If we measure each fabric while using 3-4 fabrics on the sling shot, we could me not only how tighten the slingshot was, but also which direction the player intended.

![](/images/Soft-Sensing/Screen-Shot-2019-02-14-at-2.18.35-PM.png)

However, in given time, we could only link 2 fabrics on the slingshot and linked with p5 sketch to indicate the strength.

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/294062306?h=&title=0&byline=0&portrait=0" style="position:absolute;top:0;left:0;width:100%;height:100%;" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe></div>

<br>

We used the voltage divider for Arduino part, and used serial communication for p5.js sketch.

---

# Material testing

*October 8, 2018*

Phil and I tested four different materials: Velostat/ Linqstat, Eeonyx pressure sensing fabric, Eeonyx stretch sensing fabric, and Eeonyx StaTex conductive fiber. We measured the resistance of them with a multimeter, and Arduino voltage divider circuit.

![](/images/Soft-Sensing/0.jpeg)

These soft sensing materials have tendency of ascending or descending resistance, but wasn't linear or consistent.

```
/*Voltage divider with Analogue pin 0*/
void setup() {
 Serial.begin(9600);
}

void loop() {
 // read the input on analog pin 0:
 int sensorValue = analogRead(A0);
 float voltage = sensorValue*5;
 Serial.println(voltage);
 delay(100);
}
```

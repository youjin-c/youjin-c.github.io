[ ](https://cargo.site)

[ ︎ ](/Left-Nav)

[ ]()

**[Youjin Chung](Home)**  
  
[︎](https://www.linkedin.com/in/youjin-chung/) | [︎](mailto:yjc433@nyu.edu) | [︎](https://github.com/youjinChung)   
  
[#ML](https://youjin.io/ML)  
[#XR](https://youjin.io/XR)  
[#Data](https://youjin.io/Data)  
[#Interactive](https://youjin.io/Interactive)  
  
[Archive](blog-1)  
  
  
  
**[](Resume)**[](https://www.linkedin.com/in/youjin-chung/)

# Object Segmentation  

  

  
  
Welcome to my Object Segmentation project, where I utilized machine learning
to accurately detect and segment oranges and limes in images. This project
aims to demonstrate the power of object segmentation using machine learning
and how it can be applied to improve image analysis.  
  

## Object Segmentation

  
Object segmentation is the process of identifying and isolating specific
objects within an image. For this project, I utilized MobileNetV2 to
accurately detect and segment oranges and limes in images.  
  

## Dataset

![](images/Object-Segmentation/coco_cat.png)

  
To train the models, I used a variety of datasets, including ImageNet and
Fruits 360, to obtain the necessary images of oranges and limes. Additionally,
I utilized the COCO dataset, which contains 80 categories of objects, to train
the models to recognize oranges in images.

![](images/Object-Segmentation/coco_ex.png)

  
  

## Labeling

![](images/Object-Segmentation/labeling.png)  

For labeling, I used various tools, including LabelBox, Label Studio, and
Diffgram. I found that LabelBox was the best tool for uploading large datasets
and had better iPad usability. I encountered challenges, such as dealing with
various textured limes and reviewing submitted annotations, but found that
using MAL was helpful in speeding up the labeling process.  
  

## Training

  

The models were trained on a custom additional training set that I created
using various fruit datasets. Additionally, I employed Model-assisted labeling
(MAL) to speed up the labeling process and reduce the time and effort required
to train the models. I utilized AWS EC2 p3.8xlarge, which is equipped with
four Tesla V100s of 64GB GPU memory, to perform the training.  
  

## Orange and Lime Segmentation

  
For orange segmentation, I utilized MobileNetV2 and trained the model on the
COCO dataset for oranges, achieving an accuracy of 94% on 1699 images. The
segmented oranges are colored in a rainbow pattern, making them easy to
distinguish from other objects. I also created a lime segmentation model using
MobileNetV2, which showed 70% accuracy when trained on ~200 lime images. This
model will be used for MAL in LabelBox.  

  

  

## Conclusion

  
In summary, my Object Segmentation project demonstrates the power of machine
learning for accurately detecting and segmenting oranges and limes in images.
Through the use of various tools, including MobileNetV2, and datasets,
including COCO, ImageNet, and Fruits 360, I was able to train accurate models
for object segmentation. I also learned about the importance of labeling
conventions and conversions, the benefits of open-source datasets, and the
potential for labeling group projects using labeling platforms with AI
labeling features. I hope this project inspires further research and
applications in the field of computer vision.  

2022  

[ Emotion Detection ](/Emotion-Detection)

[ML](/ML)

[ Smile Filter ](/Smile-Filter)

[ML](/ML)

[ DoodlAR ](/DoodlAR)

[XR](/XR), [ML](/ML)

[ Toonify ](/Toonify)

[ML](/ML)

[ Object Segmentation ](/Object-Segmentation)

[ML](/ML)

[ Motion Recognition ](/Motion-Recognition)

[ML](/ML), [Data](/Data)

[ The Tree of Babel ](/The-Tree-of-Babel)

[ML](/ML), [Data](/Data)

[ Posture & Eye Care ](/Posture-Eye-Care)

[ML](/ML), [Data](/Data)

[ Smile Face-in ](/Smile-Face-in)

[ML](/ML), [Data](/Data)


# Project 1 : Gender Classification
by Alexander Maximilian


#### Introduction
The uprising of technological adavancement on digital platforms, has increased the needs for analytical tools and which has become an integral part of many commercial applications. 
For example, social media has transformed to become more automated in predicting user preferences based on various characteristics, such as race, political views, interests, gender, sexual orientation, and others.
With the increasing ease of data collection becoming one of the dominant factors, methods of gender classification through facial image analysis are often used.
In this context, accuracy becomes a crucial aspect, alongside the efficient use of resources that provides economic benefits for those utilizing this technology. 

Despite the simplicity of gender classification tasks, the model required still accounts on the power of the processing unit. Based on this reason, it is decided to use an early yet decently powerful architecture namely VGG to develop this system. VGG (Visual Geometry Group) was built by Karen Simonyan and Andrew Zisserman on purpose in the ImageNet Large Scale Visual Recognition Challenge (ILSVRC) 2014, as an advancement from its predecessor AlexNet with greater depth. Using small convolutional filters (3x3) in a deep architecture, consisting of 11 to 19 layers. The design is uniform, with convolutional layers followed by ReLU activation functions and max-pooling, then fully connected layers and a softmax/binary classifier.

![VGG Architecture](https://miro.medium.com/max/850/1*_Lg1i7wv1pLpzp2F4MLrvw.png)

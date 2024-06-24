# Project 1 : Gender Classification
by Alexander Maximilian


## Introduction
The uprise of technological adavancement on digital platforms, has increased the needs for analytical tools and which has become an integral part of many commercial applications. 
For example, social media has transformed to become more automated in predicting user preferences based on various characteristics, such as race, political views, interests, gender, sexual orientation, and others.
With the increasing ease of data collection becoming one of the dominant factors, methods of gender classification through facial image analysis are often used.
In this context, accuracy becomes a crucial aspect, alongside the efficient use of resources that provides economic benefits for those utilizing this technology. 

Despite the simplicity of gender classification tasks, the model required still accounts on the power of the processing unit. Based on this reason, it is decided to use an early yet decently powerful architecture namely VGG to develop this system. VGG (Visual Geometry Group) was built by Karen Simonyan and Andrew Zisserman on purpose in the ImageNet Large Scale Visual Recognition Challenge (ILSVRC) 2014, as an advancement from its predecessor AlexNet with greater depth. Using small convolutional filters (3x3) in a deep architecture, consisting of 11 to 19 layers. The design is uniform, with convolutional layers followed by ReLU activation functions and max-pooling, then fully connected layers and a softmax/binary classifier.

<p>
  <img src="https://machinelearningknowledge.ai/wp-content/uploads/2020/08/Keras-Implementation-of-VGG16-Architecture-2.jpg" alt="Description of the image">
  <br>
  <em>Figure 1: VGG Architecture.</em>
</p>

The objectives of this project:
- **Modeling**: To build an architecture for gender classification based on the researched model.
- **Optimization**: To compare and adjust parameters to achieve accurate predictions and efficient resource usage.
- **Deployment**: To develop a basic system that can be practically used for gender classification cases.

## Getting Started
### File Description
- **Dataset**: Contains images, tabular attributes (images file name, label, index).
- **Program**: Contains .ipynb file, .py file for model deployment using streamlit.
- **Output** Folder: Saved .pth files for each of the resulting trained model, dataloaders, and initial state/weight of the models, .csv files from train test val split.
### How to Run
1. Since the model development was conducted by using Kaggle Notebook, go to kaggle.com -> Create -> New Dataset.
2. Upload data pop-up will be appeared, pick the zip of all the files inside **Dataset** folder.
3. Click on the New Notebook widget, the dataset will be shown on the right side. On the upper tab, Files -> Import Notebook -> pick the retrieved .ipynb file from the **Program** folder.
4. Click on three dots option -> Accelerator -> your choice of GPU.
5. Run all the cell. After the whole runtime is finished, in the output segment on the right side of the panel it will be found .pth files same as in the **Output** folder as well as .csv files.
6. If there is any issue occured in the middle of the runtime. Use the output files to modify the input of the dataset, hence the training process doesn't need to be strated from the very beginning. Try to modify some part of the code, especilly in the data path and to load the saved .pth models/dataloaders/initial_state etc.
7. Additional comments and details is served inside the .ipynb program, enjoy!

## Result

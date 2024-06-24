# Project 1 : Gender Classification
by Alexander Maximilian


## Introduction
The uprise of technological adavancement on digital platforms, has increased the needs for analytical tools and which has become an integral part of many commercial applications. 
For example, social media has transformed to become more automated in predicting user preferences based on various characteristics, such as race, political views, interests, gender, sexual orientation, and others.
With the increasing ease of data collection becoming one of the dominant factors, methods of gender classification through facial image analysis are often used.
In this context, accuracy becomes a crucial aspect, alongside the efficient use of resources that provides economic benefits for those utilizing this technology. 

Despite the simplicity of gender classification tasks, the model required still accounts on the power of the processing unit. Based on this reason, it is decided to use an early yet decently powerful architecture namely VGG to develop this system. VGG (Visual Geometry Group) was built by Karen Simonyan and Andrew Zisserman on purpose in the ImageNet Large Scale Visual Recognition Challenge (ILSVRC) 2014, as an advancement from its predecessor AlexNet with greater depth. Using small convolutional filters (3x3) in a deep architecture, consisting of 11 to 19 layers. The design is uniform, with convolutional layers followed by ReLU activation functions and max-pooling, then fully connected layers and a softmax/binary classifier.
![image](https://machinelearningknowledge.ai/wp-content/uploads/2020/08/Keras-Implementation-of-VGG16-Architecture-2.jpg)

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
6. If there is any issue occured in the middle of the runtime. Use the output files to modify the input of the dataset, hence the training process doesn't need to be started from the very beginning. Try to modify some part of the code, especilly in the data path and to load the saved .pth models/dataloaders/initial_state etc.
7. Enjoy!

## Result
### Preprocessing
In this project, two type of VGG architecture were employed, VGG16 and VGG19 by using Pytorch library. The dataset itself is originalled retrieved from the CelebA datasat, which already limited to 5017 images, and resized to 178 x 208 px.
![image](https://github.com/alexandermaxim8/VGG-Gender-Classifier/assets/143409662/01bb0055-c52d-4e06-882f-5a1ac5096880)

In short, before starting the model training, images inside Images folder are filtered based on index inside list_attribute_new.txt (the cleansed version of list_attribute.txt). Also only two properties are used, "202599" and "Male". Subsequently, train test val split is done with the ratio of 7:1.5:1.5. Since the train data has a claas imbalance, the data with majority class are reduced to the same number of the minority class. 
![image](https://github.com/alexandermaxim8/VGG-Gender-Classifier/assets/143409662/5154bc20-60e5-44d8-a32f-c2f73c0c160c)

It is also important to incorporate additional augmentation to enrich the knowledge of the model, initial randomized transformation with 0.2 probability:
![image](https://github.com/alexandermaxim8/VGG-Gender-Classifier/assets/143409662/4cc30967-51c0-403c-a686-77872573c0d0)

### Evaluation
To optimize the model, some parameters in the optimizer were varied. Since the first architecture VGG uses mini-batches gradient descent, in this opportunity the more adaptive apporach which are RMSProp and ADAM are chosen. Some settings of learning rate and momentum were also tested out. Here is a table showing the configuration and results:
![image](https://github.com/alexandermaxim8/VGG-Gender-Classifier/assets/143409662/53c6ff6f-041b-4fd1-a119-87e625193874)
*yellow: above threshold (accuracy F1 >= 0.9, training time <= 110s, inference time <= 0.2s, epoch <= 6)
*orange: best score

Four major properties are examined, accuracy, F1 Score, Training time, Inference time, and additional for epochs needed for convergency (due to not so accuration assesment).
The result shows, upon the whole configuration VGG16 with Adam optimizer either with learning rate of 0.00005 or 0.0001 give the best overall performance for gender classification, regardless of abnormal training time needed for lr=0.0001 or 8 epochs for lr = 0.00005. This aligns logically, where a model with less depth also requires less time in training and prediction. Adam, a more complete version of optimizer than RMSProp in general, also correlates with the more accurate result of the model.

VGG16, lr = 0.0001 results output:
![image](https://github.com/alexandermaxim8/VGG-Gender-Classifier/assets/143409662/6cb0613c-9957-4b71-9bc9-dc68405071b3)
![image](https://github.com/alexandermaxim8/VGG-Gender-Classifier/assets/143409662/edc59b41-bffc-48e5-a1d9-c9a69bf58c60)
![image](https://github.com/alexandermaxim8/VGG-Gender-Classifier/assets/143409662/c482b852-5974-421e-8bb7-cda701aa6bd4)
Find out more for others in the .ipynb file

Further exploration:
- Inspection of graphical features those dominantly learnt by the model.
- More experimentation on the regularization techniques inside the hidden layer.

## Contact
If you have any questions:
alexandermaxim8@gmail.com



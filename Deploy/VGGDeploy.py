import streamlit as st
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import torch
from torchvision import models
from torchvision import transforms
import torch.nn as nn

@st.cache_resource
def load_model():
    model = models.vgg16()
    model.classifier[6] = nn.Linear(4096, 1)
    model.load_state_dict(torch.load("vgg16.pth"))
    model.eval()
    return model

def preprocess_func(img):
    transform = transforms.Compose([
        transforms.Resize(224),
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
    ])
    image = transform(img)
    image = image.unsqueeze(0)
    return image

def make_prediction(model, processed_img):
    with torch.no_grad():
        outputs = model(processed_img)
        outputs = outputs.squeeze(1)
        prob = torch.sigmoid(outputs)*100
        predicted = (torch.sigmoid(outputs) > 0.5).float()
        if prob>50:
            label = "Male"
        else:
            label = "Female"
            prob = 100-prob
    return predicted, label, prob

## Dashboard GUI
st.title("VGG-16 Image Gender Classifier")
upload = st.file_uploader(label="Upload Image:", type=["png", "jpg", "jpeg"])

if upload:
    img = Image.open(upload)

    model = load_model()
    preprocessed_img = preprocess_func(img)
    predict, label, prob = make_prediction(model, preprocessed_img)

    main_fig = plt.figure(figsize=(6,3))
    plt.imshow(img)
    st.text(f'Gender: {label}\nwith {np.squeeze(prob.numpy()):.2f}% predicition probability')
    st.pyplot(main_fig, use_container_width=True)
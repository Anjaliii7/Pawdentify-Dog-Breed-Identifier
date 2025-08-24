# 🐶 Pawdentify: Dog Breed Prediction  

## Overview - 
**Pawdentify** is a deep learning-based web application that predicts the breed of a dog from an uploaded image.  
It uses a Convolutional Neural Network (CNN) trained on a dog breed dataset and is deployed with **Streamlit** for an interactive user experience.  

## Features - 
- Upload any dog image and get instant predictions.  
- Supports multiple dog breeds (customizable).  
- Provides probability scores for each breed.  
- Deployed using **Streamlit** with a user-friendly interface.  

## Project Architecture - 
1. **Data Preprocessing** – Image resizing, normalization, train-test split.  
2. **Model Training** – CNN model built with TensorFlow/Keras.  
3. **Model Saving** – Saved in `.keras`  format for deployment.  
4. **Deployment** – Integrated with Streamlit for easy access.  

### Model Details
- **Framework**: TensorFlow/Keras  
- **Architecture**: Custom CNN (Conv2D, MaxPooling, Dropout, Dense layers)  
- **Optimizer**: Adam  
- **Loss Function**: Categorical Crossentropy  
- **Training Techniques**: Early Stopping & Model Checkpoint  


import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
def load_model():
    model = tf.keras.models.load_model("dog_breed.keras")
    return model

model = load_model()

dog_names =['scottish_deerhound','maltese_dog','afghan_hound','entlebucher','bernese_mountain_dog']

# Streamlit UI

st.set_page_config(page_title="🐶 Dog Breed Prediction", page_icon="🐾", layout="centered")

st.title("🐶 Pawdentify - Dog Breed Prediction")
st.write("Upload a picture of a dog.")

# Upload Image
uploaded_file = st.file_uploader("Choose a dog image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess image
    st.write("Processing...")
    img = image.resize((224, 224))   # Adjust size to match your model
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # Prediction
    predictions = model.predict(img_array)
    predicted_class = dog_names[np.argmax(predictions)]
    confidence = np.max(predictions) * 100

    # Show results
    st.success(f"Predicted Breed: **{predicted_class}**")
    st.write(f"Confidence: **{confidence:.2f}%**")

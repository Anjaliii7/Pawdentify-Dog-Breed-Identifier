import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf

# -------------------------------
# Load your trained model
# -------------------------------
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("dog_breed.keras")
    return model

model = load_model()

# -------------------------------
# Define class names
# -------------------------------
CLASS_NAMES = ['scottish_deerhound','maltese_dog','afghan_hound','entlebucher','bernese_mountain_dog']

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="🐶 Dog Breed Prediction",
    page_icon="🐾",
    layout="wide"
)

# -------------------------------
# Custom Styling
# -------------------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
        font-family: 'Segoe UI', sans-serif;
    }
    h1 {
        color: #2e2e2e;
        text-align: center;
        font-size: 3em !important;
    }
    .result-card {
        background: white;
        padding: 20px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0px 4px 25px rgba(0,0,0,0.15);
        margin-top: 20px;
    }
    .confidence-label {
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------
# Title
# -------------------------------
st.markdown("<h1>🐾 Dog Breed Prediction App 🐾</h1>", unsafe_allow_html=True)
st.write("<p style='text-align:center;'>Upload a picture of a dog, and let AI guess its breed 🐕✨</p>", unsafe_allow_html=True)

# -------------------------------
# Upload Image
# -------------------------------
uploaded_file = st.file_uploader("📸 Upload a dog image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display image
    image = Image.open(uploaded_file)
    col1, col2, col3 = st.columns([3,3,3])  # middle column is bigger
    with col2:
        st.image(image, caption="📷 Uploaded Image", width=300)



    # Preprocess image
    img = image.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Prediction
    predictions = model.predict(img_array)
    predicted_class = CLASS_NAMES[np.argmax(predictions)]
    confidence = np.max(predictions) * 100

    # Show results (simple + clean)
    st.markdown(
        f"""
        <div class="result-card">
            <p style="font-size:22px;">🐶 Predicted Breed: <b>{predicted_class}</b></p>
            <div class="confidence-label">Confidence: {confidence:.2f}%</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Confidence bar
    st.progress(int(confidence))







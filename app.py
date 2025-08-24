import streamlit as st
from PIL import Image

# Page configuration
st.set_page_config(page_title="Pawdentify - Dog Breed Prediction", page_icon="🐶", layout="wide")

# Title with custom styling
st.markdown(
    """
    <div style="text-align:center; padding:20px;">
        <h1 style="color:#4CAF50; font-size:50px;">🐾 Pawdentify 🐾</h1>
        <h3 style="color:#555;">Dog Breed Prediction Made Easy</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.markdown("📌 Use the options below to explore Pawdentify:")

menu = st.sidebar.radio("Go to", ["Home", "Upload & Predict", "About"])

if menu == "Home":
    st.markdown(
        """
        <div style="text-align:center; padding:20px;">
            <h2>Welcome to Pawdentify 🐶</h2>
            <p style="font-size:18px; color:#333;">
                Upload your dog’s photo and let our AI model predict its breed instantly!
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    cols = st.columns(3)
    with cols[0]:
        st.image("https://placedog.net/400/300?id=15", caption="Golden Retriever", use_container_width=True)
    with cols[1]:
        st.image("https://placedog.net/400/300?id=25", caption="Pug", use_container_width=True)
    with cols[2]:
        st.image("https://placedog.net/400/300?id=35", caption="Beagle", use_container_width=True)

elif menu == "Upload & Predict":
    st.markdown("### 📤 Upload an Image")
    uploaded_file = st.file_uploader("Choose a dog image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        st.markdown("### 🔍 Prediction Result")
        # Dummy prediction for demo (replace with your model prediction)
        st.success("Predicted Breed: **Golden Retriever** 🐕")

        st.progress(85)  # confidence bar

elif menu == "About":
    st.markdown(
        """
        ## 📖 About Pawdentify
        Pawdentify is a deep learning project built with **TensorFlow/Keras** and deployed using **Streamlit**.
        
        **Model Details:**
        - Framework: TensorFlow/Keras  
        - Architecture: Custom CNN (Conv2D, MaxPooling, Dropout, Dense layers)  
        - Optimizer: Adam  
        - Loss Function: Categorical Crossentropy  
        - Early Stopping & Model Checkpoint applied during training  

        🚀 Developed with ❤️ for dog lovers!
        """
    )


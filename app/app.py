# Streamlit app
import streamlit as st
from PIL import Image

from utils import load_model, predict_image

# ==========================================
# PAGE CONFIG
# ==========================================
st.set_page_config(
    page_title="DermAI Skin Cancer Classifier",
    page_icon="🩺",
    layout="centered"
)

# ==========================================
# TITLE
# ==========================================
st.title("🩺 DermAI Skin Cancer Classifier")

st.markdown(
"""
Upload a skin lesion image and let the model predict the disease category.
"""
)

# ==========================================
# LOAD MODEL
# ==========================================
model = load_model()

# ==========================================
# IMAGE UPLOADER
# ==========================================
uploaded_file = st.file_uploader(
    "Choose an image...",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    if st.button("Predict"):

        predicted_class, confidence = predict_image(
            model,
            image
        )

        st.success(f"Prediction: {predicted_class}")

        st.info(
            f"Confidence: {confidence:.2f}%"
        )
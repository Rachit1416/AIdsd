import streamlit as st
from PIL import Image

st.title("🕺 AI Dance Step Detector")

uploaded_file = st.file_uploader("Upload your dance pose image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.success("Image uploaded successfully!")

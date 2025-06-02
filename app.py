import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
from PIL import Image

st.title("🕺 AI Dance Step Detector")

uploaded_file = st.file_uploader("Upload a dance pose image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert PIL image to OpenCV format
    image_np = np.array(image)
    image_np = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    # Pose estimation using MediaPipe
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(static_image_mode=True)
    results = pose.process(cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB))

    if results.pose_landmarks:
        st.success("Pose landmarks detected!")

        # Draw landmarks
        mp_drawing = mp.solutions.drawing_utils
        mp_drawing.draw_landmarks(image_np, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Convert back to PIL to display
        result_image = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)
        st.image(result_image, caption="Pose Detected", use_column_width=True)
    else:
        st.warning("Could not detect pose landmarks. Try a clearer full-body image.")

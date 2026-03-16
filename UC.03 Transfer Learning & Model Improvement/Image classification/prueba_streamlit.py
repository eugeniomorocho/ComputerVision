import streamlit as st
st.title("Image Classification with Transfer Learning")
st.write("This is a simple Streamlit app for image classification using transfer learning. Upload an image to see the predicted class.")
file = st.file_uploader("Choose an image...")
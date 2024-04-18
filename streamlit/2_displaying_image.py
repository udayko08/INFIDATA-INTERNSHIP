import streamlit as st
from PIL import Image
img = Image.open("kiccha.jpg")
st.title("Displaying Image")
st.image(img,width=350)
st.header("Sudeep Sanjeev")
st.subheader("Kiccha Sudeepa")
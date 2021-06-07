import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from matplotlib import pyplot as plt
import os
from PIL import Image

st.title("Abuela")


#@st.cache
uploaded_file = st.file_uploader("Upload a photo")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    #label = predict(uploaded_file)
    st.write('%s (%.2f%%)' % (label[1], label[2]*100))


def process_image(image_path):
	pass

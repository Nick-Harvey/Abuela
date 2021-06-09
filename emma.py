import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from matplotlib import pyplot as plt
from google.cloud import storage
import os
from PIL import Image

# App libraries
from app.object_store import objectStore as objectstore

# Gcloud bucket 
client = storage.Client()
# https://console.cloud.google.com/storage/browser/[bucket-id]/
bucket = client.get_bucket('dev-abuela-input-images')

st.title("Abuela")
st.text("These are my grandparents Emma and Raul. In the early 60's they immigrated from Cuba to the US to escape Castro begin a new life.")


#@st.cache
uploaded_file = st.file_uploader("Upload a photo")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    objectstore.upload_blob(bucket.name, uploaded_file, uploaded_file.name)
    st.write("Processing...")
    #label = predict(uploaded_file)
    #st.write('%s (%.2f%%)' % (label[1], label[2]*100))


def process_image(image_path):

	pass
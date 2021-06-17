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

# Start of Streamlit App
# Convert this to an actual Main function later
st.title("Abuela")
st.markdown(
    "These are my grandparents Emma and Raul. In the early 60's they immigrated from Cuba to the US to escape Castro and his army."
    )

# Add the Static Hero Image
hero_image = Image.open('imgs/static/Emma_and_Raul.jpg')
st.image(hero_image)


def process_image(image_path):
    

    pass


with st.sidebar.form("Restore"):
    st.write("Start Here")
    ## Upload file 
    uploaded_file = st.file_uploader("Upload a Photo you want to restore.")

    if uploaded_file is not None:
        objectstore.upload_blob(bucket.name, uploaded_file, uploaded_file.name)

    enhance_options = st.multiselect(
        "Photo Enhancement Options",
        ["General restore", "Restore damaged photo (ie cracks)", "Colorize"]
    )

    # Submit the form
    submitted = st.form_submit_button("Submit")

    if 'General restore' in enhance_options:
        if submitted:
            process_image(uploaded_file)
    else:
        pass




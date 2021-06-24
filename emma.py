import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from matplotlib import pyplot as plt
from google.cloud import storage
import os
from PIL import Image

bucket = "abuela_input_images_dev"

# App libraries
from app.object_store import objectStore as objectstore
# Jaruco is the hometown my grandmother is from in Cuba.
# She is the insipiration for this project.
from app.pipelines import Jaruco as Jaruco


# Start of Streamlit App
# Convert this to an actual Main function later
st.title("Hi, Abuela!")
# st.markdown(
#     "##Step 1."
#     )
# st.markdown(
#     "Pick a photo you want to restore."
#     )

'''
## Step 1.
Pick a photo you want to restore
'''

uploaded_file = st.file_uploader("Max image size 650x650 (temp issue due to gpu limits)")


## Process the Photo
if uploaded_file is not None:
    #Display the photo that will get enhanced
    image = Image.open(uploaded_file)


    st.write("This is the image that will get upgraded.")
    st.image(image)

    st.markdown(
        "Step2. Choose what you want done."
        )

    with st.form("Choose Restore Option"):
        st.write("Choose the type of restore")
        general_restore = st.checkbox("General Restore", value= False)
        general_restore_with_cracks = st.checkbox("General Restore With Cracks", value=False)
        
        if general_restore:
            objectstore.upload_blob(bucket, uploaded_file, uploaded_file.name)
            Jaruco.general_restore(uploaded_file)
            # Upload it to gcloud

        if general_restore_with_cracks:
            Jaruco.general_restore_with_cracks(uploaded_file)

        submitted = st.form_submit_button("Restore")

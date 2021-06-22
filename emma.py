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
# Jaruco is the hometown my grandmother is from in Cuba.
# She is the insipiration for this project. She'll my 
# OG IT Abuela (She managed datacenters in the 70's)
from app.pipelines import Jaruco as Jaruco


# Start of Streamlit App
# Convert this to an actual Main function later
st.title("Hi, Abuela!")
st.markdown(
    "Step1. Pick a Photo you would like to restore."
    )

uploaded_file = st.file_uploader("Upload a Photo you want to restore.")


## Process the Photo
if uploaded_file is not None:
    #Display the photo that will get enhanced
    image = Image.open(uploaded_file)
    
    # Upload it to gcloud

    objectstore.upload_blob(uploaded_file)


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
            Jaruco.general_restore(uploaded_file)

        if general_restore_with_cracks:
            Jaruco.general_restore_with_cracks(uploaded_file)

        submitted = st.form_submit_button("Restore")

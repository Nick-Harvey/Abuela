import streamlit as st
import numpy as np
import pandas as pd
import time
import plotly.express as px
from matplotlib import pyplot as plt
from google.cloud import storage
import os
from PIL import Image

gen_restore_bucket = "abuela_input_images_dev"
scratches_bucket = "abuela_input_images_scratches_dev"

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


st.sidebar.write(
    '''
    ## Step 1.
    Pick a photo you want to restore
    '''
    )


uploaded_file = st.sidebar.file_uploader("Max image size 650x650 (temp issue due to gpu limits)")


## Process the Photo
if uploaded_file is not None:
    #Display the photo that will get enhanced
    image = Image.open(uploaded_file)


    st.write("This is the image that will get upgraded.")
    st.image(image)

    '''
    ## Step 2.
    Choose what type of restore you want to apply
    '''

    with st.form("Choose Restore Option"):
        restore_type = st.radio("Pick one", ['General Restore', 'General Restore With Cracks'])
        submitted = st.form_submit_button("Restore") 

        if submitted:
            if restore_type == 'General Restore' :
                objectstore.upload_blob(gen_restore_bucket, uploaded_file, uploaded_file.name)
                Jaruco.general_restore(uploaded_file)
                # Upload it to gcloud
            elif restore_type == 'General Restore With Cracks':
                objectstore.upload_blob(scratches_bucket, uploaded_file, uploaded_file.name)
                Jaruco.general_restore_with_cracks(uploaded_file)
            else:
                pass
            
            with st.spinner('Restoring...'):
                time.sleep(5)
                st.success('Done!')

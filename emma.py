import streamlit as st
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os

st.title("Abuela")

with st.form("my_form"):
	st.write("Choose a Photo")
	st.file_uploader('File uploader')
	st.form_submit_button(label="Process")
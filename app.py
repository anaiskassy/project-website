import streamlit as st
import requests
import pandas as pd
import numpy as np
from PIL import Image
'''
# IMAGE RESTORATION - batch #1907
'''


'''
## Load an image to start :
'''
uploaded_file = st.file_uploader("Choose an image")
_1,_2,_3 = st.columns(3)
with _2 :
    if uploaded_file is not None:
        up_image = np.array(Image.open(uploaded_file))
        st.image(up_image)


    damage = st.select_slider(
        "Select a percentage of deterioration",
        options=["5%","10%", "25%", "50%", "75%"])

'''
## Predictions :
'''
if st.button("Apply") :
    left, center, right = st.columns(3)
    array_2 = np.load("array_2.npy")

    with left :
        st.subheader('Uploaded image')
        if uploaded_file is not None:
            st.image(up_image)
        else :
            st.image(array_2)

    with center :
        st.subheader('Damaged image')
        st.image(array_2)

    with right :
        st.subheader('Predicted image')
        st.image(array_2)

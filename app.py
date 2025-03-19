import streamlit as st
import requests
import numpy as np
from PIL import Image
from io import BytesIO
'''
# IMAGE RESTORATION - batch #1907
'''
url = 'https://data-restoration-models-159309351831.europe-west1.run.app'
url_local = 'http://127.0.0.1:8000'

'''
## Load an image to start :
'''
uploaded_file = st.file_uploader("Choose an image")
_1,_2,_3 = st.columns(3)
with _2 :
    if uploaded_file is not None:
        image_bytes = BytesIO(uploaded_file.read())
        up_image = Image.open(uploaded_file).resize((64,64))
        st.image(Image.open(uploaded_file))


    model_selection = st.select_slider(
        "Select a model to try",
        options=["model 1","model 2", "model 3", "model 4"])

    explanations = {
        'model 1' : ['model de base avec output complet - petits démons - 17 000 entraînements sur 30 000 images',1],
        'model 2' : ['model de base avec output partiel - 19 000 entraînements sur 30 000 images',2],
        'model 3' : ["model complexe d'encodage et décodage - 14 000 entraînements sur 30 000 images",3],
        'model 4' : ["model complexe d'encodage et décodage combiné - 150 000 entraînements sur 30 000 images",4]
    }

st.write(f'{model_selection} : {explanations[model_selection][0]}')
model = explanations[model_selection][1]

'''
## Predictions :
'''
if st.button("Apply") :
    left, center, right = st.columns(3)
    array_2 = np.load("array_2.npy")
    image_damaged = None
    image_rebuild = None


    if uploaded_file is not None:

        image_damaged_byt = requests.post(url+'/preproc',files={'file':image_bytes}).content
        image_rebuild_byt = requests.get(url+'/predict',params={'model':model}).content

        image_damaged = Image.open(BytesIO(image_damaged_byt)).resize((300,300))
        image_rebuild = Image.open(BytesIO(image_rebuild_byt)).resize((300,300))

    with left :
        st.subheader('Uploaded image')
        if uploaded_file is not None:
            st.image(up_image.resize((300,300)))
        else :
            st.image(array_2)

    with center :
        st.subheader('Damaged image')
        if image_damaged is not None:
            st.image(image_damaged)
        else :
            st.image(array_2)

    with right :
        st.subheader('Predicted image')
        if image_rebuild is not None:
            st.image(image_rebuild)
        else :
            st.image(array_2)

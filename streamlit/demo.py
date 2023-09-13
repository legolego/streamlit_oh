import streamlit as st
from PIL import Image
from pathlib import Path

def getPathInStreamlitDir():
    return Path(__file__).parents[1] / str('streamlit/')


st.title('This is a test of Streamlit cloud from Deepnote through Github')

st.markdown('Hello World!')

img_name = 'smile.jpg'
img_path = getPathInStreamlitDir() / str('assets/' + img_name)
image = Image.open(img_path)


st.image(image)
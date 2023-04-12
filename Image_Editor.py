import streamlit as st
from PIL import Image
from PIL.ImageFilter import *

st.set_page_config(
  page_title="Image Editor",
  page_icon="📷",
  layout="wide"
)

st.markdown("---")
st.markdown("<h1 style='text-align: center;'>Image Editor</h1>", unsafe_allow_html=True)
st.markdown("---")

image = st.file_uploader("Selecione a imagem", type=["jpg", "png", "jpeg"])

info = st.empty()

size = st.empty()
mode = st.empty()
format_ = st.empty()

if image:
    img = Image.open(image)

    info.markdown("<h2 style='text-align: center;'>Information</h2>", unsafe_allow_html=True)

    size.markdown(f"<p>Size: {img.size}</p>", unsafe_allow_html=True)
    mode.markdown(f"<p>Mode: {img.mode}</p>", unsafe_allow_html=True)
    format_.markdown(f"<p>Format: {img.format}</p>", unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center;'>Resizing</h2>", unsafe_allow_html=True)
    width = st.number_input("Width", value=img.width)
    new_height = width * img.height // img.width
    height = st.number_input("Height", value=new_height)

    st.markdown("<h2 style='text-align: center;'>Rotation</h2>", unsafe_allow_html=True)
    degree = st.number_input("Degree")

    st.markdown("<h2 style='text-align: center;'>Filters</h2>", unsafe_allow_html=True)
    filters = st.selectbox("Filter", options=["None", "BLUR", "DETAIL", "EMBOSS", "SMOOTH"])
   
    s_btn = st.button("Submit")
    if s_btn:
        col1, col2 = st.columns(2)

        col1.markdown("<h6 style='text-align: center;'>Original</h6>", unsafe_allow_html=True)
        col1.image(img)
        edited = img.resize((width, height)).rotate(degree)
        
        filtered = edited

        if filters != "None":
            if filters == "BLUR":
                filtered = edited.filter(BLUR)
            elif filters == "DETAIL":
                filtered = edited.filter(DETAIL)
            elif filters == "EMBOSS":
                filtered = edited.filter(EMBOSS)
            elif filters == "SMOOTH":
                filtered = edited.filter(SMOOTH)

        col2.markdown("<h6 style='text-align: center;'>Edited</h6>", unsafe_allow_html=True)
        col2.image(filtered)
import streamlit as st
from PIL import Image

st.set_page_config(
  page_title="Image Editor",
  page_icon="📷",
  layout="wide"
)

st.markdown("---")
st.markdown("<h1 style='text-align: center;'>Image Editor</h1>", unsafe_allow_html=True)
st.markdown("---")

image = st.file_uploader("Selecione a imagem", type=["jpg", "png", "jpeg"])

size = st.empty()
mode = st.empty()
format_ = st.empty()

if image:
    img = Image.open(image)
    size.markdown(f"<p>Size: {img.size}</p>", unsafe_allow_html=True)
    mode.markdown(f"<p>Mode: {img.mode}</p>", unsafe_allow_html=True)
    format_.markdown(f"<p>Format: {img.format}</p>", unsafe_allow_html=True)
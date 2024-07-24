import streamlit as st
from PIL import Image
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
import torch

captioning_model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
feature_extractor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

st.title("Image Caption Generator")
st.write("Upload an image to generate a caption.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "webp"])

if uploaded_file is not None:

    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded Image", use_column_width=True)

    pixel_values = feature_extractor(images=img, return_tensors="pt").pixel_values

    caption_ids = captioning_model.generate(pixel_values, max_length=16, num_beams=4, early_stopping=True)
    caption = tokenizer.decode(caption_ids[0], skip_special_tokens=True)

    st.write("### Generated Caption:")
    st.write(caption)

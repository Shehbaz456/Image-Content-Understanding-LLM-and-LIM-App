from dotenv import load_dotenv
load_dotenv() 

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load gemini pro vision model and get response
model = genai.GenerativeModel('gemini-pro-vision') 
def get_gemini_response(input_text, image):
    if input_text and image:
        response = model.generate_content([input_text, image])
    elif image:
        response = model.generate_content(image)
    elif input_text:
        response = model.generate_content(input_text)
    else:
        response = "Please provide input text and/or upload an image."
    return response.text 

# Initialize Streamlit app
st.set_page_config(page_title="Gemini image Demo")
st.header("Gemini LIM Application")

# User input
input_text = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Display uploaded image
image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Button for generating response
submit = st.button("Tell me about the image")

# Generate response when button is clicked
if submit:
    if input_text or image:
        response = get_gemini_response(input_text, image) 
        st.subheader("The response is ")
        st.write(response)
    else:
        st.error("Please provide input text and/or upload an image.")










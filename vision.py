import streamlit as st
import os
from dotenv import load_dotenv
from pathlib import Path
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load .env from the same folder as vision.py
load_dotenv(Path(__file__).with_name(".env"))

print("API key loaded:", bool(os.getenv("GOOGLE_API_KEY")))



# Read the API key
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("API key not found. Check your .env file.")
    st.stop()

genai.configure(api_key=api_key)

## function to load gemini pro model and get responses

model = genai.GenerativeModel("gemini-3.8-flash")
def get_gemini_response(input, image):
    if input != "":
        response=model.generate_content([input, image])
    else:
        response=model.generate_content(image)
    return response.text

#initialise our streamlit app
st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini Application")
input=st.text_input("Input Prompt: ",key="input")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])
image = ""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image.", width="stretch")

submit = st.button("Tell me about the image")

##if submit is clicked 
if submit:
    response = get_gemini_response(input,image)
    st.subheader("The response is:")
    st.write(response)
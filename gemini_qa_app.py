from dotenv import load_dotenv
load_dotenv()         #loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load gemini pro model and get responses

model = genai.GenerativeModel("gemini-3.8-flash")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

#initialise our streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")
input = st.text_input("Input: ",key="input")
submit = st.button("Ask the Question")

## when submit is clicked 
if submit:
    response = get_gemini_response(input)
    st.subheader("The response is: ")
    st.write(response)
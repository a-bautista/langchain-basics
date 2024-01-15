import langchain_helper as lch
import streamlit as st

st.title("Translate languages")

input_lang = st.sidebar.selectbox("Select your language", ("English", "Spanish"))
output_lang = st.sidebar.selectbox("Select your language", ("Italian", "French"))
text = st.sidebar.text_area(label="Input message", max_chars=200)
response = lch.generate_names(text, input_lang, output_lang)
st.text(response)
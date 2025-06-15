
import streamlit as st
import requests

st.title("Creative AI Agent")

option = st.selectbox("Choose Command", ["/storm", "/map"])
input_text = st.text_area("Input Theme or Idea")

if st.button("Run Command"):
    if option == "/storm":
        res = requests.post("http://localhost:5000/storm", json={"theme": input_text})
        st.json(res.json())
    elif option == "/map":
        res = requests.post("http://localhost:5000/map", json={"idea": input_text})
        st.json(res.json())

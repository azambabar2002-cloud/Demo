import streamlit as st
import httpx

st.title("Hackathon Test")
if st.button("Check backend"):
    r = httpx.get("http://127.0.0.1:8000/health")
    st.write(r.json())
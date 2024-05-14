import streamlit as st
import requests


st.set_page_config(
    page_title="Fish Finder", page_icon=":fishing_pole_and_fish:", layout="centered"
)

with st.container():
    st.markdown(
        "<h2 style='text-align: center;'>Washington Fish Finder</h2>",
        unsafe_allow_html=True,
    )

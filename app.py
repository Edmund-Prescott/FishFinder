import streamlit as st
import requests


st.set_page_config(
    page_title="WA Fish Finder", page_icon=":fishing_pole_and_fish:", layout="centered"
)

with st.container():
    st.markdown(
        "<h2 style='text-align: center;'>Washington Fish Finder</h2>",
        unsafe_allow_html=True,
    )

with st.container():
    address = st.text_input("Enter starting address:")

with st.container():
    counties = [
        "All counties",
        "King",
        "Pierce",
        "Snohomish",
    ]

    lake_types = ["All lakes", "Lowland lakes", "High lakes", "Overabuntant lakes"]

    fish = [
        "All fish",
        "Black crappie",
        "Bluegill",
        "Brook trout",
        "Brown bullhead",
        "Brown trout",
        "Coastal cuttroat trout",
        "Cutthroat trout",
        "Golden trout",
        "Lake trout",
        "Largemouth bass",
        "Rainbow trout",
        "Redside shiner",
        "Tiger muskie",
        "Tiger trout",
        "Westslope cutthroat trout",
        "Yellow perch",
    ]

    county = st.selectbox("Select a county", counties)
    lake_type = st.selectbox("Select a lake type", lake_types)
    fish_variety = st.selectbox("Select fish varieties", fish)

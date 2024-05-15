import streamlit as st
import requests

st.set_page_config(
    page_title="WA Fish Finder", page_icon=":fishing_pole_and_fish:", layout="centered"
)


@st.cache_data
def read_api_key(file_path):
    try:
        with open(file_path, "r") as file:
            api_key = file.read().strip()
        return api_key
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


api_key = read_api_key("my_api_key.txt")

with st.container():
    st.markdown(
        "<h2 style='text-align: center;'>Washington Fish Finder</h2>",
        unsafe_allow_html=True,
    )


def get_place_autocomplete(input_text, api_key):
    endpoint = "https://maps.googleapis.com/maps/api/place/autocomplete/json"
    params = {
        "input": input_text,
        "key": api_key,
        "types": "address",  # You can adjust this parameter based on your needs
    }

    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        predictions = response.json().get("predictions", [])
        suggestions = [prediction["description"] for prediction in predictions]
        return suggestions
    else:
        st.error(f"Error: {response.status_code}, {response.text}")
        return []


with st.container():
    # add on change method
    address_input = st.text_input("Enter starting address:")

    # Use a reactive function to update the dropdown options based on the input
    @st.cache_data
    def get_address_suggestions(input_text):
        if input_text:
            return get_place_autocomplete(input_text, api_key)
        else:
            return []

    address_suggestions = get_address_suggestions(address_input)

    if address_suggestions:
        selected_address = st.selectbox("Select address:", address_suggestions)
        st.write("You selected:", selected_address)
    else:
        st.write("No suggestions available.")

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

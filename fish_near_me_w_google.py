import requests
import time


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


def get_travel_time(api_key, origin_address, destination_coordinates):
    # Base URL for Google Distance Matrix API
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?"

    # Parameters for the API request
    params = {
        "origins": origin_address,
        "destinations": f"{destination_coordinates[0]},{destination_coordinates[1]}",
        "key": api_key,
        "departure_time": "now",  # Requesting travel time with current traffic
    }

    # Send the request to the Google Distance Matrix API
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        # Extract the travel time from the API response
        if data["rows"][0]["elements"][0]["status"] == "OK":
            travel_time = data["rows"][0]["elements"][0]["duration_in_traffic"]["text"]
            return travel_time
        else:
            return "No route found"
    else:
        return f"Error: {response.status_code}"


api_key = read_api_key("my_api_key.txt")

# Example usage
origin_address = "1600 Amphitheatre Parkway, Mountain View, CA"
destination_coordinates = (37.7749, -122.4194)  # Coordinates for San Francisco, CA

travel_time = get_travel_time(api_key, origin_address, destination_coordinates)
print(f"Travel time: {travel_time}")

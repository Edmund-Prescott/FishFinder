import requests


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
        print(f"Error: {response.status_code}, {response.text}")
        return []


# Example usage
if __name__ == "__main__":
    api_key = "YOUR_GOOGLE_PLACES_API_KEY"
    input_text = "1600 Amphitheatre"
    suggestions = get_place_autocomplete(input_text, api_key)
    print("Suggestions:", suggestions)

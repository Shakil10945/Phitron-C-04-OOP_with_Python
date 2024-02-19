import requests
import time
import json

# Replace with your chosen API's base URL
API_BASE_URL = "https://api.example.com/"

# Replace with your chosen API key
API_KEY = "..."

# Your Dhaka city coordinates
latitude = 23.7103
longitude = 90.4070

# Function to build the API request URL
def build_url(endpoint, params):
    url = API_BASE_URL + endpoint
    for key, value in params.items():
        url += f"&{key}={value}"
    return url

# Function to retrieve weather data from the API
def get_weather_data():
    endpoint = "weather/current"  # Replace with the proper endpoint for your API
    params = {"lat": latitude, "lon": longitude, "appid": API_KEY}  # Adjust parameters as needed
    url = build_url(endpoint, params)

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.text)
            return data
        else:
            print("Error:", response.status_code)
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Main function to collect and store weather data every 30 minutes
def weather_data():
    while True:
        try:
            data = get_weather_data()
            if data:
                # Process and store weather data here (e.g., print, write to file, database)
                print(f"Current weather in Dhaka, Bangladesh:")
                # Extract and display relevant data based on your API's response structure
                # Add code to process/store data as needed
                print("-" * 30)  # Separator

        except Exception as e:
            print(f"Error: {e}")

        # Wait for 30 minutes before next request
        time.sleep(1800)  # 1800 seconds = 30 minutes

# Run the function to start collecting weather data
weather_data()

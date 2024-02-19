import requests
import json
import time

def weather_data():
    api_key = 'YOUR_API_KEY'
    city = 'YOUR_CITY_NAME'
    base_url = 'https://api.openweathermap.org/data/2.5/weather'

    while True:
        try:
            # Construct the API URL with your city and API key
            url = f"{base_url}?q={city}&appid={api_key}"

            # Send a GET request to the API
            response = requests.get(url)

            # Check if the request was successful
            if response.status_code == 200:
                # Parse the JSON response
                data = json.loads(response.text)

                # Extract relevant weather information
                temperature = data['main']['temp']
                description = data['weather'][0]['description']

                # Print the weather information
                print(f"Weather in {city}: Temperature {temperature}°C, Description: {description}")

            else:
                print(f"Failed to fetch weather data. Status code: {response.status_code}")

            # Sleep for 30 minutes before fetching data again
            time.sleep(1800)  # 1800 seconds = 30 minutes

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            # Sleep for 30 minutes even if there's an error
            time.sleep(1800)

if __name__ == "__main__":
    weather_data()

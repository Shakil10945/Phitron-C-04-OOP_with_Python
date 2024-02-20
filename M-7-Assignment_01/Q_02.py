import requests
import json
import time

def weather_data():
    api_key = 'YOUR_API_KEY'
    city = 'YOUR_CITY_NAME'
    base_url = 'https://api.openweathermap.org/data/2.5/weather'

    while True:
        try:
            url = f"{base_url}?q={city}&appid={api_key}"
            response = requests.get(url)

            if response.status_code == 200:

                data = json.loads(response.text)

                temperature = data['main']['temp']
                description = data['weather'][0]['description']


                print(f"Weather in {city}: Temperature {temperature}°C, Description: {description}")

            else:
                print(f"Failed to fetch weather data. Status code: {response.status_code}")

            time.sleep(1800)  

        except Exception as e:
            print(f"An error occurred: {str(e)}")

            time.sleep(1800)

    weather_data()


import requests
import json
import PyWallpaper

# Replace 'YOUR_API_KEY' with your actual NASA API key
api_key = "YOUR_API_KEY"

# API endpoint URL
api_url = f"https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

try:
    # Make a request to the API
    response = requests.get(api_url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Parse the JSON content
    data = response.json()

    # Extract the image URL
    image_url = data['url']

    # Download the image
    image_response = requests.get(image_url)
    image_response.raise_for_status()  # Raise an exception for HTTP errors

    # Save the image to a file
    with open('apoddd.png', 'wb') as image_file:
        image_file.write(image_response.content)

    # Set the wallpaper
    PyWallpaper.change_wallpaper(r"./apoddd.png")

except requests.RequestException as e:
    print(f"Error during request: {e}")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
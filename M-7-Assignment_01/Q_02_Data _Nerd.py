import requests
import json

url = "https://www.weatherapi.com/weather/q/dhaka-174248"

req = requests.get(url)

response = req.json()
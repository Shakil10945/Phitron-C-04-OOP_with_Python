"""
Problem:
Download and  Cange desktop wallpapers automatically
"""
import requests
import json
api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
response = requests.get(api_url)

content = response.content.decode('UTF-8')

dict_content=json.loads(content)

image_url= dict_content['url']

res = requests.get(image_url)
print(res)

with open('apod.png', 'wb') as image:
    image.write(res.content)
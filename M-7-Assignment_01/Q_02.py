import requests
import json
import time

#input the api 
api_url = "https://www.weatherapi.com/weather/q/dhaka-174248"

#Access the api through requests.
response = requests.get(api_url)
 
 #get the content through response.content
content = response.content
#we have got the dsata in the byte form till now
#now convert the data into "string" form
content2= content.decode('UTF-8')
dict_content = json.loads(content2)
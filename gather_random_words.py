import requests
import os
from dotenv import load_dotenv
load_dotenv()

url = "https://wordsapiv1.p.rapidapi.com/words/"

querystring = {"random":"true"}

headers = {
    'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
    'x-rapidapi-key': os.getenv("API_KEY")
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
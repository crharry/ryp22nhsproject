import requests

URL = "https://www.google.com"
request = requests.get(URL)
print(request.headers)
print(request.text)
import requests

URL="http://127.0.0.1:8000/data"

r=requests.get(url=URL)
data=r.json()

print(data)
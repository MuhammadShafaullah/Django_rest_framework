import requests
import json

URL="http://127.0.0.1:8000/dataCrate/"

data={
    'name':'Ali',
    'roll': 4465,
    'city': 'Lodhran'
}
mydata= json.dumps(data)

r=requests.post(url=URL, data=mydata)
data=r.json()
print(data)

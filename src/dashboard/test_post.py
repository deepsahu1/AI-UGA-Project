import requests

data = {"data" : "data recieved"}

response = requests.post("http://127.0.0.1:8051/post-sensor-data", json=data)


print(response.json())
import requests

BASE = 'http://localhost:1337/'

response = requests.get(BASE + 'heartbeat')
print(response.json())
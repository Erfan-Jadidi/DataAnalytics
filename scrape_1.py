import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")

data = response.json()

print(data)
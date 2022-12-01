import requests

result = requests.get("http://jsonplaceholder.typicode.com/todos")
result = result.text

print(result)

print(type(result))
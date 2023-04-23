import requests
endpoint = "http://127.0.0.1:8000/product"
response = requests.post(endpoint, json={'name':'pasteque', 'content':'just pasteque', 'prix':200})
print(response.json())
print(response.status_code)

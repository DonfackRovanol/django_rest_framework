import requests
endpoint = "http://127.0.0.1:8000/product/update/8/"
response = requests.put(endpoint, json={'name':'poivron300', 'content':'', 'prix':10000})
print(response.json())
print(response.status_code)

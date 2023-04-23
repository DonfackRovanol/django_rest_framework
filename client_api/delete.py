import requests
endpoint = "http://127.0.0.1:8000/product/delete/8/"
response = requests.delete(endpoint)
print(response.status_code)

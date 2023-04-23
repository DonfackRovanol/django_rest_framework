import requests
#from getpass import getpass
#endpoint = "http://127.0.0.1:8000/api/auth"
#username = input('entrez votre username:\n')
#password = getpass('entrez votre password:\n')
#auth_response = requests.post(endpoint, json={'username':username, 'password':password})
#print(auth_response.json())

#if auth_response.status_code == 200:
endpoint = "http://127.0.0.1:8000/product/create-list/"
headers = {
    'Authorization': 'Bearer 2bd8d1023d911b80b766c8cf8db29bddd142bf78'
}
response = requests.get(endpoint, headers=headers)
print(response.json())
print(response.status_code)   

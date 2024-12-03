import requests 

# Point d'entree
endpoint = " http://127.0.0.1:8000/api/"
response = requests.get(endpoint, params={'hh': 22}, json={'query': 'hello'})
# response = requests.get(endpoint, data={'query': 'hello'})
print(response.json())
print(response.status_code) 
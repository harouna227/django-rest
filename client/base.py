import requests 

# Point d'entree
endpoint = " http://127.0.0.1:8000/produit/api/"
response = requests.get(endpoint)
# response = requests.get(endpoint, data={'query': 'hello'})
print(response.json())
print(response.status_code) 
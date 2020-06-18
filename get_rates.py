import requests
response = requests.get("http://api.exchangeratesapi.io/latest?symbol=USD")
print(response.text)
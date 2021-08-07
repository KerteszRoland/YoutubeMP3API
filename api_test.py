import requests

endpoint="http://localhost:5000/mp3"
payload={
    "url":"https://www.youtube.com/watch?v=TupN1EBcguE"
}
response = requests.get(endpoint, params=payload).json()
print(response)
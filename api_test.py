import requests

endpoint="http://localhost:5000/mp3"
payload={
    "url":"https://www.youtube.com/watch?v=dQw4w9WgXcQ"
}
response = requests.get(endpoint, params=payload).json()
print(response)
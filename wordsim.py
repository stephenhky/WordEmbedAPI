import requests

url = 'http://localhost:5000/mostsimilarvector'
r = requests.post(url, json={'pos1': 'man', 'pos2': 'woman', 'neg': 'king'})

print(r.json())
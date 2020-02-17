
import numpy as np
import requests

url = 'http://localhost:5000'

r = requests.post(url+'/mostsimilarvector', json={'pos1': 'man', 'pos2': 'woman', 'neg': 'king'})
print(r.json())

r = requests.post(url+'/vectorsize', json={})
print(r.json())

r = requests.post(url+'/wordvector', json={'word': 'physics'})
print(np.array(r.json()['vector']))

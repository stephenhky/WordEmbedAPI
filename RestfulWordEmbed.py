
import numpy as np
import requests

class RestfulWordEmbedModel:
    def __init__(self, url):
        self.url = url

    def getvector(self, token):
        r = requests.post(self.url+'/wordvector', json={'word': token})
        vector = np.array(r['vector'])
        return vector

    def getvectorsize(self):
        r = requests.post(self.url + '/vectorsize', json={})
        vecsize = r['vectorsize']
        return vecsize

    def __getitem__(self, item):
        return self.getvector(item)
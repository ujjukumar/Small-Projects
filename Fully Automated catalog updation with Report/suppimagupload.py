#!/usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"

path = 'supplier-data/images/'

for item in os.listdir(path):
    f, e = os.path.splitext(item)
    file = os.path.join(path, item)
    if e == '.jpeg':
        with open(file, 'rb') as opened:
            r = requests.post(url, files={'file': opened})

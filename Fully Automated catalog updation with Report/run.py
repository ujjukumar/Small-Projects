#! /usr/bin/env python3

import os
import requests
import json

path = "supplier-data/descriptions/"

files_list = os.listdir(path)

for file in files_list:
    text_file_name = os.path.join(path, file)
    f, e = os.path.splitext(file)
    image_file = f + '.jpeg'
    with open(text_file_name) as f:
        description_dict = {}
        description_dict["name"] = f.readline().rstrip("\n")
        description_dict["weight"] = f.readline().rstrip(" lbs\n")
        description_dict["description"] = f.readline().rstrip("\n")
        description_dict["image_name"] = image_file

        web_address = "http://35.225.83.71/fruits/"
        response = requests.post(web_address, data=description_dict)
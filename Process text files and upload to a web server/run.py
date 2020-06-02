#! /usr/bin/env python3

import os
import requests
import json

path = "/data/feedback"

files_list = os.listdir(path)

for file in files_list:
    file_name = os.path.join(path, file)
    with open(file_name) as f:
        feedback_dict = {}

        feedback_dict["title"] = f.readline().rstrip("\n")
        feedback_dict["name"] = f.readline().rstrip("\n")
        feedback_dict["date"] = f.readline().rstrip("\n")
        feedback_dict["feedback"] = f.readlines()[0].rstrip("\n")

        web_address = "http://104.154.72.176/feedback/"
        response = requests.post(web_address, data=feedback_dict)
        print(response.status_code)

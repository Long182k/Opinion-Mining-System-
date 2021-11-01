# Lấy Json -> Parse -> Insert DB -> dsda
import json


with open('labels.json') as file:
    distros_dict = json.load(file)

for distro in distros_dict:
    print(distro['Name'])
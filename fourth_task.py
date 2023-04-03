import json
import os, glob
from datetime import datetime

file = input("Введите название json файла")
data = ...
with open(file, 'r') as json_file:
    data = json.load(json_file)
    for i in data:
        i['updated'] = datetime.strptime(i['updated'], 'iso')

with open(file, 'r+') as json_file:
    json.dump(data, json_file)

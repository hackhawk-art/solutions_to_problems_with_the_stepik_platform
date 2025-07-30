from collections import ChainMap
import json

with open("files_json/zoo.json", encoding="utf-8") as file:
    data = json.load(file)
    print(ChainMap(data))
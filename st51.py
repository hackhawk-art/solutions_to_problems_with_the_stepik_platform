import json

with open("data1.json", encoding="utf-8") as file:
    content1 = json.load(file)
with open("data2.json", encoding="utf-8") as file:
    content2 = json.load(file)
with open("data_merge.json", "w", encoding="utf-8") as result:
    answ = content1 | content2
    json.dump(answ, result, indent=3)
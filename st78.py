from collections import Counter
import csv

with open("name_log.csv", encoding="utf-8") as file:
    data = {}
    rows = file.read()
    for i in rows.split("\n")[1:]:
        key = i.split(",")[1]
        value = (i.split(",")[0], i.split(",")[2])
        data.update({key: []})
    for i in rows.split("\n")[1:]:
        key = i.split(",")[1]
        value = (i.split(",")[0], i.split(",")[2])
        data[key].append(value)
    for k, v in sorted(data.items(), key=lambda x: x[0]):
            print(f"{k}: {len(v)}")

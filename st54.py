import json
import csv

with open("playgrounds.csv", encoding="utf-8") as file:
    rows = file.read()
    result = {}
    keys = []
    for i in rows.split("\n")[1:]:
        result.update({i.split(";")[1]: {}})
        keys.append(i.split(";")[1])
    for i in rows.split("\n")[1:]:
        for j in range(len(keys)):
            result[i.split(";")[1]].update({i.split(";")[2]: []})
    for k, v in result.items():
        for j in v.keys():
            for i in rows.split("\n")[1:]:
                if i.split(";")[2] == j:
                    v[j].append(i.split(";")[3])
    with open("addresses.json", "w", encoding="utf-8") as res:
        json.dump(result, res, indent=3)

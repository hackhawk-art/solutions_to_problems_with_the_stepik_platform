import json

with open("countries.json", encoding="utf-8") as file:
    data = json.load(file)
    result = {}
    for i in data:
        result.update({i["religion"]: []})
    for i in data:
        for j in result.keys():
            if i["religion"] == j:
                result[i["religion"]].append(i["country"])
    with open("religion.json", "w", encoding="utf-8") as res:
        json.dump(result, res, indent=3)
import json

with open("people.json", encoding="utf-8") as file:
    data = json.load(file)
    patter = max(data, key=len)
    result = []
    for i in data:
        for k, v in patter.items():
            i[k] = i.get(k, None)
        result.append(i)
    with open("updated_people.json", "w", encoding="utf-8") as res:
        json.dump(result, res)

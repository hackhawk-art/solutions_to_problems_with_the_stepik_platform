import json

with open("food_services.json", encoding="utf-8") as file:
    data = json.load(file)
    my_dict = {}
    result = []
    for i in data:
        if i["TypeObject"] not in my_dict.keys():
            my_dict.update({i["TypeObject"]: []})
    for i in data:
        for k in my_dict.keys():
            if i["TypeObject"] == k:
                my_dict[i["TypeObject"]].append([i["Name"], i["SeatsCount"]])
    for k, v in my_dict.items():
        max_val = 0
        for i in v:
            if i[1] > max_val:
                max_val = i[1]
                name = i[0]
        result.append([k, name, max_val])
    for i in sorted(result, key=lambda x: x[0]):
        print(f"{i[0]}: {i[1]}, {i[2]}")
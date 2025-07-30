import json

with open("food_services.json", encoding="utf-8") as file:
    data = json.load(file)
    names = []
    my_dict = {}
    for i in data:
        names.append(i["District"])
    for i in names:
        my_dict.update({i: names.count(i)})
    for k, v in my_dict.items():
        if v == max(my_dict.values()):
            print(f"{k}: {v}")
    names1 = []
    result = {}
    for i in data:
        if i["IsNetObject"] == "да":
            names1.append(i["OperatingCompany"])
    for i in names1:
        result.update({i: names1.count(i)})
    for k, v in result.items():
        if v == max(result.values()):
            print(f"{k}: {v}")
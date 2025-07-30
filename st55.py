import json
import csv

with open("students.json", encoding="utf-8") as file:
    data = json.load(file)
    names = []
    phones = []
    for i in data:
        if i["age"] >= 18 and i["progress"] >= 75:
            names.append(i["name"])
            phones.append(i["phone"])
    my_dict = dict(zip(names, phones))
    columns = ["name", "phone"]
    with open('data.csv', 'w', encoding='utf-8', newline='') as result:
        writer = csv.writer(result)
        writer.writerow(columns)
        for k, v in sorted(my_dict.items()):
            writer.writerow([k, v])
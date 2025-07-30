import csv

with open("salary_data.csv", encoding="utf-8") as file:
    rows = file.read()
    keys = []
    values = []
    for i in rows.split("\n")[1:]:
        if i.split(";")[0] in keys:
            values.append(int(i.split(";")[1]))
        elif i.split(";")[0] not in keys:
            keys.append(i.split(";")[0])
    comp = dict(zip(keys, values))
    print(comp)
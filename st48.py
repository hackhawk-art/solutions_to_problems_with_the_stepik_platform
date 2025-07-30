import csv

with open("prices.csv", encoding="utf-8") as file:
    rows = file.read()
    names = rows.split("\n")[0]
    my_dict = {}
    keys = []
    values = []
    for i in rows.split("\n")[1:]:
        mini_list = []
        for j in range(len(names)):
            try:
                keys.append(names.split(";")[j])
                mini_list.append(i.split(";")[j])
            except:
                break
        values.append(mini_list)

    for i in range(len(keys)):
        my_dict.update({keys[i]: []})

    for i in range(1, len(keys)+1):
        for j in values:
            try:
                if int(j[i]) == min(j):
                    my_dict[keys[i]].append(int(j[i]))
            except:
                continue
    names = []
    for i in range(1):
        for j in values:
            try:
                names.append(j[i])
            except:
                continue
    del my_dict["Магазин"]
    result = []
    for k, v in my_dict.items():
        for j in range(len(v)):
            if v[j] == min(v):
                print(f"{k}: {names[j]}")
import csv

with open("salary_data.csv", encoding="utf-8") as file:
    rows = file.read()
    my_dict = {}
    names = []
    result = {}
    for i in rows.split("\n")[1:]:
        names.append(i.split(";")[0])
        if i.split(";")[0] in my_dict.keys():
            my_dict[i.split(";")[0]] += int(i.split(";")[1])
        elif i.split(";")[0] not in my_dict.keys():
            my_dict.update({i.split(";")[0]: int(i.split(";")[1])})
    for i in rows.split("\n")[1:]:
        if i.split(";")[0] in my_dict.keys():
            result.update({i.split(";")[0]: my_dict[i.split(";")[0]] / names.count(i.split(";")[0])})
    for i in sorted(result.items(), key=lambda x: (x[1], x[0])):
        print(i[0])
import csv

with open("wifi.csv", encoding="utf-8") as file:
    rows = file.read()
    my_dict = {}
    for i in rows.split("\n")[1:-1]:
        if i.split(";")[1] in my_dict.keys():
            my_dict[i.split(";")[1]] = int(my_dict[i.split(";")[1]]) + int(i.split(";")[-1])
        elif i.split(';')[1] not in my_dict.keys():
            my_dict.update({i.split(";")[1]: i.split(";")[-1]})
    for k, v in sorted(my_dict.items(), key=lambda x: (-int(x[1]), x[0])):
        print(f"{k}: {str(v)}")

import csv

with open("titanic.csv", encoding="utf-8") as file:
    rows = file.read()
    mens = []
    girls = []
    for i in rows.split("\n")[1:]:
        mini_list = i.split(";")
        if int(mini_list[0]) == 1 and mini_list[2] == "male" and float(mini_list[3]) < 18:
            mens.append(mini_list[1])
        elif int(mini_list[0]) == 1 and mini_list[2] == "female" and float(mini_list[3]) < 18:
                girls.append(mini_list[1])
    for i in mens:
        print(i)
    for i in girls:
        print(i)
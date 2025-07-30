from datetime import datetime
import csv

with open("name_log.csv", encoding="utf-8") as file:
    with open("new_name_log.csv", "w", encoding="utf-8", newline='') as jope:
        writer = csv.writer(jope)
        rows = file.read()
        my_dict = {}
        result = []
        for i in rows.split("\n")[1:]:
            mini_list = i.split(',')
            if mini_list[1] in my_dict.keys():
                my_dict[mini_list[1]].append([mini_list[0], mini_list[2]])
            elif mini_list[1] not in my_dict.keys():
                my_dict.update({mini_list[1]: [[mini_list[0], mini_list[2]]]})
        result = []
        for k, v in my_dict.items():
            if len(v) == 1:
                result.append([k, v])
            elif len(v) > 1:
                result.append([k, max(v, key=lambda x: datetime.strptime(x[1], "%d/%m/%Y %H:%M"))])
        num_1 = ["username"]
        num_2 = ["email"]
        num_3 = ["dtime"]
        writer.writerow(num_1 + num_2 + num_3)
        for i in sorted(result):
            if len(i[1]) == 1:
                for j in i[1]:
                    writer.writerow([j[0], i[0], str(j[1])])
            elif len(i[1]) > 1:
                writer.writerow([i[1][0], i[0], str(i[1][1])])
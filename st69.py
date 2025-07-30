from datetime import datetime
import csv

with open("meetings.csv", encoding="utf-8") as file:
    rows = file.read()
    my_list = []
    for i in rows.split("\n")[1:]:
        my_list.append(i.split(","))
    for i in sorted(my_list, key=lambda x: (datetime.strptime(x[2], "%d.%m.%Y"), (datetime.strptime(x[3], "%H:%M")))):
        print(i[0], i[1])
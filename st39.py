import csv

n = int(input())
with open("deniro.csv", encoding="utf-8") as file:
    rows = file.read()
    my_list = []
    for i in rows.split("\n"):
        try:
            my_list.append([i.split(",")[0], i.split(",")[1], i.split(",")[2]])
        except:
            break
    for i in sorted(my_list, key=lambda x: int(x[n - 1]) if n > 1 else x[n - 1]):
        print(f"{i[0]},{i[1]},{i[2]}")
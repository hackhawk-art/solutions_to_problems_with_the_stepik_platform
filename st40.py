import csv

def csv_columns(filename):
    with open(filename, encoding="utf-8") as file:
        rows = file.read()
        names = rows.split("\n")[0]
        my_d_keys = []
        my_d_values = []
        for i in range(len(names.split(","))):
            my_d_keys.append(names.split(",")[i])
            my_d_values.append([])
        my_dict = dict(zip(my_d_keys, my_d_values))
        for i in rows.split("\n")[1:]:
            for j in range(len(names.split(","))):
                my_dict[names.split(",")[j]].append(i.split(",")[j])
        return my_dict
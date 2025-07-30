import csv

with open("student_counts.csv", encoding="utf-8-sig") as file:
    with open("sorted_student_counts.csv", "w", encoding="utf-8-sig", newline='') as result:
        writer = csv.writer(result)
        rows = file.read()
        keys = (rows.split("\n")[0]).split(",")
        my_keys = []
        my_values = []
        for i in rows.split("\n")[1:]:
            for j in range(len(keys)):
                if keys[j] == "year":
                    keys[j] = "1-1"
                else:
                    my_keys.append(keys[j])
                    my_values.append([])
        my_dict = dict(zip(my_keys, my_values))
        for i in rows.split("\n")[1:]:
            for j in range(len(keys)):
                my_dict[keys[j]].append(i.split(",")[j])
        mini_list = []
        columns = []
        for k in sorted(my_dict.keys(), key=lambda x: (int(x.split('-')[0]), x.split('-')[1])):
                columns.append(k)
        for i in range(len(keys)):
            mina = []
            for k in sorted(my_dict.keys(), key=lambda x: (int(x.split('-')[0]), x.split('-')[1])):
                try:
                    mina.append(my_dict[k][i])
                except:
                    break
            mini_list.append(mina)
        writer.writerow(["year"] + columns[1:])
        for i in mini_list:
            writer.writerow(i)

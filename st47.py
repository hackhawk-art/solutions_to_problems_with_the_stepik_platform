import csv

def condense_csv(filename, id_name):
    with open(filename, encoding="utf-8") as file:
        with open("condensed.csv", "w", encoding="utf-8", newline='') as result:
            writer = csv.writer(result)
            rows = file.read()
            names = []
            columns = []
            for i in rows.split("\n"):
                if i.split(",")[1] not in names:
                    names.append(i.split(",")[1])
                else:
                    continue

            my_dict = {}
            for i in rows.split("\n"):
                my_dict.update({i.split(",")[0]: []})

            for i in rows.split("\n"):
                my_dict[i.split(",")[0]].append(i.split(",")[2])

            writer.writerow([id_name, *names])
            for k, v in my_dict.items():
                writer.writerow([k, *v])

print(condense_csv("text.txt", "ID"))
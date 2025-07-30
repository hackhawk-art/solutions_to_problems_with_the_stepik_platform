import csv

with open("data.csv", encoding="utf-8") as file:
    with open("domain_usage.csv", "w", encoding="utf-8", newline='') as jope:
        writer = csv.writer(jope)
        rows = file.read()
        keys = []
        values = []
        for i in rows.split("\n")[1:]:
            keys.append((i.split(",")[2]).split("@")[1])
        for i in keys:
            values.append(keys.count(i))
        my_dict = dict(zip(keys, values))
        xuy = ["domain"]
        jopa = ["count"]
        writer.writerow(xuy + jopa)
        for k, v in sorted(my_dict.items(), key=lambda x: (x[1], x[0])):
            writer.writerow([k,v])
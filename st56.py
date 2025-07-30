from datetime import datetime, timedelta
import json

with open("pools.json", encoding="utf-8") as file:
    data = json.load(file)
    my_dict = {}
    for i in data:
        stop = datetime.strptime((i["WorkingHoursSummer"]["Понедельник"].split("-")[1]), "%H:%M")
        start = datetime.strptime((i["WorkingHoursSummer"]["Понедельник"].split("-")[0]), "%H:%M")
        hours, minutes, seconds = str(stop - start).split(":")
        if int(hours) >= 2:
            if int(i["DimensionsSummer"]["Length"]) <= 70:
                my_dict.update({(int(i["DimensionsSummer"]["Length"]), int(i["DimensionsSummer"]["Width"])): i["Address"]})
        else:
            continue
    res = max(my_dict.items(), key=lambda x: (x[0], x[1]))
    print(f"{res[0][0]}x{res[0][1]}")
    print(res[1])
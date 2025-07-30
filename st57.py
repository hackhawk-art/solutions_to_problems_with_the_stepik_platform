from datetime import datetime
import json

with open("exam_results.csv", encoding="utf-8") as file:
    rows = file.read()
    my_dict = {}
    for i in rows.split("\n")[1:]:
        my_dict.update({(i.split(",")[0], i.split(",")[1], i.split(",")[4]): ([], [])})
    for i in rows.split("\n")[1:]:
        my_dict[(i.split(",")[0], i.split(",")[1], i.split(",")[4])][0].append(int(i.split(",")[2]))
        my_dict[(i.split(",")[0], i.split(",")[1], i.split(",")[4])][1].append(datetime.strptime(i.split(",")[3], "%Y-%m-%d %H:%M:%S"))
    result = {}
    for k, v in my_dict.items():
        value = {}
        for score, date in zip(v[0], v[1]):
            value[score] = max(value.get(score, date), date)
        result.update({k: value})
    final_file = []
    for k, v in result.items():
        key = max(v.keys())
        if max(v.keys()) == min(v.keys()) and len(v.keys()) > 1 or len(v.keys()) == 1:
            date = max(v.values())
        elif max(v.keys()) != min(v.keys()) and len(v.keys()) > 1:
            date = v[key]
        final_file.append({"name": k[0],
                           "surname": k[1],
                           "best_score": int(max(v)),
                           "date_and_time": str(date),
                           "email": k[2]})
    final_file = sorted(final_file, key=lambda x: x["email"])
    with open("best_scores.json", "w", encoding="utf-8") as res:
        json.dump(final_file, res, indent=3)
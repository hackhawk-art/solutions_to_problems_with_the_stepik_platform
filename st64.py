from zipfile import ZipFile
import json

def is_correct_json(string):
    try:
        json.load(string)
        return True
    except:
        return False

with ZipFile('data.zip') as data:
    names = []
    for elem in data.infolist():
        if not elem.is_dir():
            with data.open(elem) as data_f:
                if is_correct_json(data_f) is True:
                    data.extract(data_f.name)
                    names.append(data_f.name)
    res = []
    for i in names:
        with open(i, encoding="utf-8") as file:
            data = json.load(file)
            if data["team"] == "Arsenal":
                res.append([data["first_name"], data["last_name"]])
    for i in sorted(res, key=lambda x: (x[0], x[1])):
        print(*i)
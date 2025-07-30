from datetime import datetime

with open("diary.txt", "r", encoding="utf-8") as file:
    result = []
    for i in file.readlines():
        result.append(i)
    print(result)
from collections import Counter

with open("pythonzen.txt", encoding="utf-8") as file:
    rows = file.read()
    result = Counter()
    mini_list = []
    for i in rows.split("\n"):
        for j in i.strip(" "):
            if j.isalpha():
                mini_list.append(j.lower())
    result = Counter(mini_list)
    for k, v in sorted(result.items()):
        print(f"{k}: {v}")

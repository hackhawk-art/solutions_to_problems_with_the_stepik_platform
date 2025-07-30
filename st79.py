from collections import Counter
import json
import csv

with open("files_json/prices.json", encoding="utf-8") as prices:
    price = json.load(prices)
    result = 0
    with open("files_csv/quarter1.csv", encoding="utf-8") as file:
        rows = file.read()
        for i in rows.split("\n")[1:]:
            mini_list = [int(j) * price[i.split(",")[0]] for j in i.split(",")[1:]]
            result += sum(mini_list)
    with open("files_csv/quarter2.csv", encoding="utf-8") as file:
        rows = file.read()
        for i in rows.split("\n")[1:]:
            mini_list = [int(j) * price[i.split(",")[0]] for j in i.split(",")[1:]]
            result += sum(mini_list)
    with open("files_csv/quarter3.csv", encoding="utf-8") as file:
        rows = file.read()
        for i in rows.split("\n")[1:]:
            mini_list = [int(j) * price[i.split(",")[0]] for j in i.split(",")[1:]]
            result += sum(mini_list)
    with open("files_csv/quarter4.csv", encoding="utf-8") as file:
        rows = file.read()
        for i in rows.split("\n")[1:]:
            mini_list = [int(j) * price[i.split(",")[0]] for j in i.split(",")[1:]]
            result += sum(mini_list)
    print(result)
import csv

def condense_csv(filename, id_name):
    with open(filename, encoding="utf-8") as file:
        with open("condensed.csv", "w", encoding="utf-8", newline="") as result:


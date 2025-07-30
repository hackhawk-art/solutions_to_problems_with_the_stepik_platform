from collections import namedtuple
import pickle

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])

with open("data.pkl", "rb") as file:
    data = pickle.load(file)
    for i in data:
        for k, v in zip(Animal._fields, i):
            print(f"{k}: {v}")
        print()
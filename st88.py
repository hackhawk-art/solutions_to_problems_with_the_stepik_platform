from collections import namedtuple
from itertools import groupby

Person = namedtuple('Person', ['name', 'age', 'height'])

persons = [Person('Tim', 63, 193), Person('Eva', 47, 158),
           Person('Mark', 71, 172), Person('Alex', 45, 193),
           Person('Jeff', 63, 193), Person('Ryan', 41, 184),
           Person('Ariana', 28, 158), Person('Liam', 69, 193)]

my_dict = {}

for i in sorted(persons, key=lambda x: x.height):
    my_dict.update({i.height: []})

for i in persons:
    my_dict[i.height].append(i.name)

for k, v in my_dict.items():
    print(f"{k}: {', '.join(sorted(v))}")


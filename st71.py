from collections import defaultdict

def wins(pairs):
    my_dict = defaultdict(set)
    for i in pairs:
        my_dict[i[0]].add(i[1])
    return my_dict

result = wins([('Артур', 'Дима'), ('Артур', 'Тимур'), ('Артур', 'Анри'), ('Дима', 'Артур')])

for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))
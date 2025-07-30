from collections import ChainMap, Counter

bread = {'булочка с кунжутом': 150, 'обычная булочка': 130, 'ржаная булочка': 140}
meat = {'куриный бифштекс': 500, 'говяжий бифштекс': 700, 'рыбный бифштекс': 400}
sauce = {'сливочно-чесночный': 50, 'кетчуп': 50, 'горчица': 50, 'барбекю': 60, 'чили': 60}
vegetables = {'лук': 100, 'салат': 150, 'помидор': 150, 'огурцы': 100}
toppings = {'сыр': 250, 'яйцо': 150, 'бекон': 300}

string = Counter(str(input()).split(","))
my_dict = ChainMap(bread, meat, sauce, vegetables, toppings)
res = 0
res_lens = []
for k, v in sorted(string.items(), key=lambda x: x[0]):
    res_lens.append(f"{k.ljust(len(max(string.keys(), key=len)))} x {string[k]}")
    print(f"{k.ljust(len(max(string.keys(), key=len)))} x {string[k]}")
    res += my_dict[k] * v
itog = f"ИТОГ: {res}р"
print("-" * len(max(res_lens)) if len(itog) < len(max(res_lens)) else "-" * len(itog))
print(itog)

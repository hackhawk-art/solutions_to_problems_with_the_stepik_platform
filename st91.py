from collections import namedtuple
import itertools

n = int(input())

Item = namedtuple('Item', ['name', 'mass', 'price'])

items = [Item('Обручальное кольцо', 7, 49_000),
         Item('Мобильный телефон', 200, 110_000),
         Item('Ноутбук', 2000, 150_000),
         Item('Ручка Паркер', 20, 37_000),
         Item('Статуэтка Оскар', 4000, 28_000),
         Item('Наушники', 150, 11_000),
         Item('Гитара', 1500, 32_000),
         Item('Золотая монета', 8, 140_000),
         Item('Фотоаппарат', 720, 79_000),
         Item('Лимитированные кроссовки', 300, 80_000)]
res = []

for i in range(1, len(items) + 1):
    mini_list = []
    for j in items:
        if j.mass > n:
            continue
        else:
            mini_list.append(itertools.combinations(j.mass))
    if sum(mini_list, key=lambda x: x.mass) > n:
        continue
    else:
        mini_list.append(res)

print(res)
            

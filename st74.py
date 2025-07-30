from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ', 'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})
new_grades = OrderedDict()

for rule in [False if i % 2 == 0 else True for i in range(len(data))]:
    name, grade = data.popitem(last=rule)
    new_grades[name] = grade

print(new_grades)
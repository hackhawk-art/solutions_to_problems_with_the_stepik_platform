from datetime import date, timedelta
from calendar import isleap

def years_days(year):
    if isleap(year) == False:
        count = 0
        for i in range(365):
            res = date(year, 1, 1)
            yield res + timedelta(days=count)
            count += 1
    else:
        count = 0
        for i in range(366):
            res = date(year, 1, 1)
            yield res + timedelta(days=count)
            count += 1

dates = years_days(1900)

print(*dates)
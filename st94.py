from functools import total_ordering
from datetime import timedelta, datetime

@total_ordering
class FuzzyString(str):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, obj):
        self.string = str(obj).lower()
    
    def __eq__(self, obj):
        if isinstance(obj, FuzzyString):
            return self.string == obj.string
        elif isinstance(obj, str):
            return self.string == str(obj).lower()
        return NotImplemented
    
    def __ne__(self, obj):
        if isinstance(obj, FuzzyString):
            return self.string != obj.string
        elif isinstance(obj, str):
            return self.string != str(obj).lower()
        return NotImplemented
    
    def __lt__(self, obj):
        if isinstance(obj, FuzzyString):
            return self.string < obj.string
        elif isinstance(obj, str):
            return self.string < str(obj).lower()
        return NotImplemented
        
    def __contains__(self, obj):
        if isinstance(obj, FuzzyString):
            return obj.string in self.string
        elif isinstance(obj, str):
            return str(obj).lower() in self.string
        return NotImplemented
    
    def __ge__(self, obj):
        if isinstance(obj, FuzzyString):
            return self.string >= obj.string
        elif isinstance(obj, str):
            return self.string >= str(obj).lower()
        return NotImplemented

class UpperCaseDict(dict):
    def update(self, items):
        if isinstance(items, dict):
            items = items.items()
        for key, value in items:
            self[key] = value

    def __setitem__(self, key, value):
        key = str(key).upper()
        super().__setitem__(key, value)
    
    def __repr__(self):
        return f'{type(self).__name__}({super().__repr__()})'

start = '09:00'
duration = '01:30'
end = timedelta(hours=int(start.split(":")[0]), minutes=int(start.split(":")[1])) + timedelta(hours=int(duration.split(":")[0]), minutes=int(duration.split(":")[1]))
end = ":".join(str(end).split(":")[:-1])
time = (start, end)
print(int("08") < int(time[0].split(":")[0]))

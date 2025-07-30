class BaseClass:
    def __init__(self, start, diff):
        self.start = start
        self.diff = diff
        
    def __iter__(self):
        return self

class ArithmeticProgression(BaseClass):
    def __next__(self):
        n = self.start
        self.start += self.diff
        return n 
            
class GeometricProgression(BaseClass):
    def __next__(self):
        n = self.start
        self.start *= self.diff
        return n 
        
# TEST_1:
progression = ArithmeticProgression(0, 1)

for elem in progression:
    if elem > 10:
        break
    print(elem, end=' ')

# TEST_2:
progression = GeometricProgression(1, 2)

for elem in progression:
    if elem > 10:
        break
    print(elem, end=' ')

# TEST_3:
progression = GeometricProgression(4, -2)
count = 0

for item in progression:
    if count == 20:
        break
    count += 1
    print(item, end=' ')

# TEST_4:
progression = ArithmeticProgression(100, -10)
count = 0

for item in progression:
    if count == 20:
        break
    count += 1
    print(item, end=' ')

# TEST_5:
progression = GeometricProgression(100, 10)
count = 0

for item in progression:
    if count == 20:
        break
    count += 1
    print(item, end=' ')
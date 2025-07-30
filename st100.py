from math import sqrt

class Vector:
    def __init__(self, *args):
        self.coordinates = tuple(args)
        
    def __str__(self):
        return str(self.coordinates)
    
    def __add__(self, other):
        if isinstance(other, Vector):
            if len(self.coordinates) != len(other.coordinates):
                raise ValueError("Векторы должны иметь равную длину")
            else:
                res = []
                for i in range(len(self.coordinates)):
                    res.append(self.coordinates[i] + other.coordinates[i])
                return Vector(*tuple(res))
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, Vector):
            if len(self.coordinates) != len(other.coordinates):
                raise ValueError("Векторы должны иметь равную длину")
            else:
                res = []
                for i in range(len(self.coordinates)):
                    res.append(self.coordinates[i] - other.coordinates[i])
                return Vector(*tuple(res))
        return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self.coordinates) != len(other.coordinates):
                raise ValueError("Векторы должны иметь равную длину")
            else:
                res = []
                for i in range(len(self.coordinates)):
                    res.append(self.coordinates[i] * other.coordinates[i])
                return sum(res)
        return NotImplemented
    
    def norm(self):
        res = []
        for i in range(len(self.coordinates)):
            res.append(self.coordinates[i] ** 2)
        return sqrt(sum(res))
    
    def __eq__(self, other):
        if isinstance(other, Vector):
            if len(self.coordinates) != len(other.coordinates):
                raise ValueError("Векторы должны иметь равную длину")
            else:
                return self.coordinates == other.coordinates
        return NotImplemented
    
    def __ne__(self, other):
        if isinstance(other, Vector):
            if len(self.coordinates) != len(other.coordinates):
                raise ValueError("Векторы должны иметь равную длину")
            else:
                return self.coordinates != other.coordinates
        return NotImplemented
    
coordinates = [((64, 42, 11), (20, 40, 64)), ((50, 96, 60), (32, 26, 38)), ((46, 95, 64), (23, 70, 78)),
               ((22, 29, 48), (21, 50, 31)), ((40, 50, 19), (95, 37, 78)), ((74, 21, 77), (74, 21, 77)),
               ((55, 33, 88), (55, 33, 88)), ((99, 50, 74), (77, 28, 87)), ((64, 65, 33), (24, 73, 76)),
               ((63, 12, 36), (80, 53, 22)), ((92, 15, 80), (48, 42, 17)), ((84, 65, 80), (72, 15, 46)),
               ((54, 48, 52), (68, 25, 26)), ((37, 93, 12), (16, 76, 42)), ((45, 91, 87), (46, 91, 58)),
               ((33, 74, 85), (13, 20, 36)), ((63, 12, 43), (63, 12, 43)), ((87, 67, 41), (41, 82, 52)),
               ((10, 63, 68), (54, 36, 65)), ((74, 51, 90), (30, 25, 90))]

for coord1, coord2 in coordinates:
    vector1 = Vector(*coord1)
    vector2 = Vector(*coord2)
    print(vector1 == vector2, vector1 != vector2)

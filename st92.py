class ElectricCar:
    def __init__(self, color, owner):
        self.color = color
        self.owner = owner

car = ElectricCar('black', 'Elon')
car = ElectricCar(color='black', owner='Yan')
car = ElectricCar('black', None)
car = ElectricCar(owner='Elon', color='black')

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f'a {self.color} car'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.color!r}, {self.mileage!r})'

my_car = Car('red', 2314)
print(repr(my_car))

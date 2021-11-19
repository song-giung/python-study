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


class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


myclass = MyClass()

print(myclass.method())
print(myclass.classmethod())
print(myclass.staticmethod())


##

class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'{self.__class__.__name__}' \
               f'(' \
               f'{self.ingredients!r}' \
               f')'

    # factory method
    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])

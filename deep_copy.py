import copy

xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs)  # shallow copy(only 1 depth)

xs.append(['new_value'])

xs[0][0] = 'a'

deep_copy = copy.deepcopy(xs)

xs[0][0] = 'new'


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{self.__class__.__name__}' \
               f'({self.x}, {self.y})'

    def __eq__(self, other):
        if other.x != self.x:
            return False
        elif other.y != self.y:
            return False

        return True


a = Point(10, 20)
b = copy.copy(a)

#print(a is b)  # False 클래스의 멤버변수가 원시타입이기 때문에 copy 로도 전혀 다른 객체를 생성(복제) 가능
#print(a == b)  # True __eq__때문


class Rectangle:
    def __init__(self, topleft, bottomright):
        self.topleft = topleft
        self.bottomright = bottomright

    def __repr__(self):
        return f'{self.__class__.__name__}' \
               f'({self.topleft},{self.bottomright})'


rect = Rectangle(Point(0, 1), Point(5, 6))
srect = copy.copy(rect)

rect.topleft.x = -5

print(rect is srect)
print(rect == srect)

print(rect)
print(srect)
class Repeater:
    def __init__(self, value):
        self.value = value
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.value) <= self.count:
            raise StopIteration
        new_value = self.value[self.count]
        self.count += 1
        return new_value


my_list = [1, 2, 3]
iterator = iter(my_list)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))  # StopIteration 예외 발생


repeater = Repeater('Hello')
for next in repeater:
    print(next)
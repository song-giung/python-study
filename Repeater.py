class RepeaterIterator:
    def __init__(self, source):
        self.source = source

    def __next__(self):
        return self.source.value


class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return RepeaterIterator(self)


repeater = Repeater('Hello')
iterator = repeater.__iter__()  # 반복 가능한 iterator 객체를 얻고

# while True:
#     item = iterator.__next__()  # 값을 위해 호출
#     print(item)


# 내장 함수를 이용하여 구현
iterator = iter(repeater)
next(iterator)  # return Hello

def repeater(value):
    while True:
        yield value


print(repeater('Hey'))  # <generator object repeater at 0x101469120>


iterator = repeater('Hello')
print(next(iterator))
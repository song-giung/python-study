def repeat_three_times(value):
    yield value
    yield value
    yield value


iterator = repeat_three_times('hello')

print(next(iterator))
print(next(iterator))
print(next(iterator))
next(iterator)  # StopIteration 예외 발생


def repeat_with_counter(value, max_repeats):
    count = 0

    while True:
        if count >= max_repeats:
            return

        count += 1
        yield value


def repeat_with_counter_short(value, max_repeats):
    for i in range(max_repeats):
        yield value

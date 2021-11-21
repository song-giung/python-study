def integers():
    for i in range(10):
        yield i


def squared(seq):
    for x in seq:
        yield x * x


def negated(seq):
    for x in seq:
        yield -x


chain = negated(squared(integers()))

for x in chain:
    print(x)
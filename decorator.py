def strong(func):
    def wrapper():
        return f'<strong>{func()}</strong>'

    return wrapper


def emphasis(func):
    def wrapper():
        return f'<em>{func()}</em>'

    return wrapper


@strong  # 2
@emphasis  # 1
def greet():
    return 'hello'


def greet_with_no_decorator():
    return 'hello'


print(greet())  # <strong><em>hello</em></strong>

decorated_greet = strong(emphasis(greet_with_no_decorator))
print('no decorator : ' + decorated_greet())

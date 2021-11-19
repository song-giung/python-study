def uppercase(func):
    def wrapper():
        original_result: str = func()
        modified_result = original_result.upper()
        return modified_result

    return wrapper


@uppercase
def greet():
    return 'hello'


print(greet())  # >>> HELLO

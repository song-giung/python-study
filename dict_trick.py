import operator

name_for_userid = {
    1423: "Alice",
    12542: "Michale",
    23412: "Master Yi"
}


def greeting(userid):
    try:
        return f'Hi {name_for_userid[userid]}'
    except KeyError:
        return 'Hi there'


# default value
def greeting_short(userid):
    return f'Hi {name_for_userid.get(userid, "there")}'


# sort
dict_items = list(name_for_userid.items())

key_sorted_items = sorted(name_for_userid)
value_sorted_items = sorted(name_for_userid.items(), key=lambda x: x[1])

# 자주 사용하는 key 함수는 operator에 구현되어 있다.
sorted(name_for_userid.items(), key=operator.itemgetter(1))
sorted(name_for_userid.items(), key=operator.attrgetter('value'))


def dispatch_if(operator, x, y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y

# 함수를 호출할 때 마다 임시 dict와 익명 함수가 생성 되어 비효율적이긴 하다.
# 함수를 자주 호출 한다면 상수로 빼어 두는 것이 좋겠다.
def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()

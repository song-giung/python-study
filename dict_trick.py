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

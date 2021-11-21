import array
import collections
from types import MappingProxyType

od = collections.OrderedDict(one=1, two=2, three=2)
od.keys()

dd = collections.defaultdict(list)
dd['dogs'].append('Rufus')
dd['dogs'].append('Kathrin')

dict1 = {'one': 1, 'two': 2}
dict2 = {'three': 3, 'four': 4}
chain = collections.ChainMap(dict1, dict2)

writable = {'one': 1, 'two': 2}
read_only = MappingProxyType(writable)
# read_only['one'] = 'new_value'
## TypeError: 'mappingproxy' object does not support item assignment

## list(가변 동적)
arr = ['one', 'two', 'three']
del arr[1]

## tuple(불변)
arr = ('one', 'two', 'three')
# arr[0] = 'hello'  # error
# del arr[0]  # error
new_tuple = arr + (23,)  ## make copy

arr = array.array('f', [1, 2, 3])
arr.append(5)

# set
vowels = {'a', 'e', 'i', 'o', 'u'}
# empty set
empty_set = set()  # {} 는 dict 를 생성

letters = set('alice')
intersection = letters.intersection(vowels)
print(intersection)

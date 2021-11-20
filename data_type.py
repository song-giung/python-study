import collections
from types import MappingProxyType

od = collections.OrderedDict(one=1, two=2, three=2)
print(od.keys())

dd = collections.defaultdict(list)
dd['dogs'].append('Rufus')
dd['dogs'].append('Kathrin')
print(dd['dogs'])

dict1 = {'one': 1, 'two': 2}
dict2 = {'three': 3, 'four': 4}
chain = collections.ChainMap(dict1, dict2)
print(chain)
print(chain['three'])

writable = {'one': 1, 'two': 2}
read_only = MappingProxyType(writable)
read_only['one'] = 'new_value'
## TypeError: 'mappingproxy' object does not support item assignment

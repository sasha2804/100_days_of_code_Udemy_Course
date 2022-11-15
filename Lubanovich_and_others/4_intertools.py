import itertools

for item in itertools.chain([1,2],['a','b']):
    print(item)

# for item in itertools.cycle([1,2]):
#     print(item)
words = ['eeenie', 'meenie', 'miny', 'MO']

class UppercaseException(Exception):
    print('Uppercase')


for word in words:
    if word.isupper():
        raise Exception(word)


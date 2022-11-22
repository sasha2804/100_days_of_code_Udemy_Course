# dict_test = {'key1':1, 'key2':2}
# key_search = 'key3'

# try:
#     print(dict_test[key_search])
# except KeyError:
#     print('key not found')
#     dict_test[key_search] = 0
# else:
#     print(dict_test[key_search])
# finally:
#     print('operation has been successfully finished')
#     raise Exception('cusomised exception is raised')


# height = float(input('Enter weight: '))
# weight = float(input('Enter weight: '))

# if height > 3:
#     raise ValueError('Height cannot be more than 3 m')

# if weight > 200:
#     raise ValueError('Weight canno exceed 200 kg')

# print(weight/height**2)


fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie") 
    else:
        print(fruit + " pie")


make_pie(45)

    
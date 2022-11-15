
# from shutil import move
# from turtle import title


# some_pythons = {'Graham': 'Chapman','John': 'Cleese','Eric': 'Idle','Terry': 'Gilliam','Michael': 'Palin'}

# some_pythons1 = {'Graham1': 'Chapman','John': 'Cleese1','Eric1': 'Idle','Terry1': 'Gilliam','Michael1': 'Palin'}


# # del some_pythons1['Graham1']
# # some_pythons1.pop('Eric1')

# # print(some_pythons1.get('Graham', 'Kok'))

# # print(some_pythons1)

# # word = 'letters'

# # letter_counts = {letter: word.count(letter) for letter in set(word)}

# # print(letter_counts)

# drinks = {'martini': {'vodka', 'vermouth'}, 'black russian': {'vodka', 'kahlua'}, 'white russian': {'cream', 'kahlua', 'vodka'},'manhattan': {'rye', 'vermouth', 'bitters'},'screwdriver': {'orange juice', 'vodka'}}


# # for name, contents in drinks.items():
# #     if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
# #         print(name)
# # print('******')
# # for name, contents in drinks.items():
# #     if contents & {'vermouth', 'orange juice'}:
# #         print(name)

# # print('******')

# # for name, contents in drinks.items():
# #     if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
# #         print(name)


# #TODO 1 Создайте англо-французский словарь с названием e2f и выведите его на экран.
# e2f = {'dog':'chien', 'cat':'chat', 'walrus':'morse'}
# #TODO 2 Используя словарь e2f, выведите французский вариант слова walrus.
# print(e2f['walrus'])
# #TODO 3 Создайте французско-английский словарь f2e на основе словаря e2f. Используйте метод items.
# f2e = {}
# for key, value in e2f.items():
#     f2e[value] = key
#     # f2e[i.values()] = i.keys()
# print(f2e)
# #TODO 4 Используя словарь f2e, выведите английский вариант слова chien.
# print(f2e['chien'])
# #TODO 5 Выведите на экран множество английских слов из ключей словаря e2f.
# print(set(e2f.keys()))
# print('#################')
# #TODO 6 Создайте многоуровневый словарь life. Используйте следующие строки для ключей верхнего уровня: 
# # 'animals', 'plants' и 'other'. Сделайте так, чтобы ключ 'animals' ссылался на другой словарь, 
# # имеющий ключи 'cats', 'octopi' и 'emus'. Сделайте так, чтобы ключ 'cats' ссылался на 
# # список строк со значениями 'Henri', 'Grumpy' и 'Lucy'. 
# # Остальные ключи должны ссылаться на пустые словари.
# cats = ['Henri', 'Grumpy', 'Lucy']
# animals = {'cats': cats, 'plants': 3, 'octopi': 4}
# empty_dict = {}
# life = {'animals': animals, 'plants': empty_dict}
# print(life)
# #TODO 7 Выведите на экран высокоуровневые ключи словаря life.
# print(life.keys())
# #TODO 8 Выведите на экран ключи life['animals'].
# print(life['animals'])
# #TODO 9 Выведите значения life['animals']['cats'].
# print(life['animals']['cats'])
# #TODO 10 Используйте генератор словаря, чтобы создать словарь squares. Используйте range(10), 
# # чтобы получить ключи. 
# # В качестве значений используйте возведенное в квадрат значение каждого ключа.
# print('####################')
# squares = {}
# for i in range(10):
#     squares[i] = i**2
# print(squares)
# #TODO 11 Используйте генератор множества, чтобы создать множество odd из нечетных чисел диапазона range(10).
# print('####################')
# s = set()
# for i in range(10):
#     if i%2 != 0:
#         s.add(i)
# print(s)
# #TODO 12 Используйте включение генератора, чтобы вернуть строку 'Got ' 
# # и числа из диапазона range(10). 
# # Итерируйте по этой конструкции с помощью цикла for.

# #TODO 13 Используйте функцию zip(), чтобы создать словарь из кортежа ключей ('optimist', 'pessimist', 'troll') и 
# # кортежа значений ('The glass is half full', 'The glass is half empty', 'How did you get a glass?').
# print('####################')
# keys = ('optimist', 'pessimist', 'troll')
# values = ('The glass is half full', 'The glass is half empty', 'How did you get a glass?')
# new_struct= {}

# for key, value in zip(keys, values):
#     new_struct[key] = value
# print(new_struct)

# #TODO 14 Используйте функцию zip(), чтобы создать словарь с именем movies, 
# # в котором объединены списки titles = ['Creature of Habit', 'Crewel Fate', 'Sharks On a Plane'] и 
# # plots = ['A nun turns into a monster', 'A haunted yarn shop', 'Check your exits'].
# print('####################')
# titles = ['Creature of Habit', 'Crewel Fate', 'Sharks On a Plane']
# plots = ['A nun turns into a monster', 'A haunted yarn shop', 'Check your exits']
# movies = {}

# for key, value in zip(titles, plots):
#     movies[key] = value
# print(movies)



periodic_table = {'Hydrogen': 1, 'Helium': 2}

# carbon = periodic_table.setdefault('Carbon', 12)

# print(periodic_table['Carbon'])

# print(periodic_table)


# from collections import defaultdict

# periodic_table = defaultdict(int)

# periodic_table['Hydrogen'] = 1
# periodic_table['Lead']

# print(periodic_table['Lead'])

# from collections import defaultdict
# food_counter = defaultdict(int)
# for food in ['spam', 'spam', 'eggs', 'spam']:
#     food_counter[food] += 1

# for food, count in food_counter.items():
#     print(food, count)


from collections import Counter

breakfast = ['spam', 'spam', 'eggs', 'spam']

count = Counter(breakfast)

print(count)



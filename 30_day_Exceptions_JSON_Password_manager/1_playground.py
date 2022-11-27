# # dict_test = {'key1':1, 'key2':2}
# # key_search = 'key3'

# # try:
# #     print(dict_test[key_search])
# # except KeyError:
# #     print('key not found')
# #     dict_test[key_search] = 0
# # else:
# #     print(dict_test[key_search])
# # finally:
# #     print('operation has been successfully finished')
# #     raise Exception('cusomised exception is raised')


# # height = float(input('Enter weight: '))
# # weight = float(input('Enter weight: '))

# # if height > 3:
# #     raise ValueError('Height cannot be more than 3 m')

# # if weight > 200:
# #     raise ValueError('Weight canno exceed 200 kg')

# # print(weight/height**2)


# fruits = ["Apple", "Pear", "Orange"]

# # #TODO: Catch the exception and make sure the code runs without crashing.
# # def make_pie(index):
# #     try:
# #         fruit = fruits[index]
# #     except IndexError:
# #         print("Fruit pie") 
# #     else:
# #         print(fruit + " pie")


# # make_pie(45)

# facebook_posts = [
#     {'Likes': 21, 'Comments': 2}, 
#     {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
#     {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
#     {'Comments': 4, 'Shares': 2}, 
#     {'Comments': 1, 'Shares': 1}, 
#     {'Likes': 19, 'Comments': 3}
# ]

# total_likes = 0

# for post in facebook_posts:
#     try:
#         total_likes += post['Likes']
#     except KeyError:
#         pass
    


# print(total_likes)

# x = 'AdddfdfrdRRTTt'

# print(x.capitalize())
    
x = 'brandaa'

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}



print(thisdict[x])


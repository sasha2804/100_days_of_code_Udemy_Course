# lst = [0,1,2,2,2,3,0,4,2]
# lst = [0,1,8,8,8,3,0,4,2,2]


lst = [0,1,2,3,4]

x = 0

for i in range(0, len(lst) - x):

    if i == 2:
        lst.remove(lst[i])
        x += 1
        print('!!!!!')

    print(lst[i])


# s = "abcabcbb"

# s = "bbbbbbb"

s='pwwkew'

max_len = 0
count = 0
s_temp = ''


for i in s:
    if i not in s_temp:
        s_temp += i
        count += 1
        print(s_temp)
        # print(i)
        # print('1')
    else:
        s_temp = s_temp[-1]
        print(s_temp)
        if count > max_len:
            max_len = count
            count = 0
            # print('end')


print('max len: ', max_len)



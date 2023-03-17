# s = "abcabcbb"

# s = "bbbbbbb"

# s='pwwkew'

# s = "au"

# s = "aab"

s = "dvdfg"

# s = "abcabcbb"

# s = 'vdvfg'

# s = '   '

# s="pwwkew"

# s="aaaaaaaaaaa"

max_len = 0
count = 0
s_temp = ""
count1 = 0

# s="pwwkew"
s="abctgabcd"

s = "abba"
# s = 'cdd'

# s = "auda"

if len(s) == 1:
    s = s*2

for i in s:
    count1 += 1          
    if i not in s_temp:
        s_temp += i
        print('s_temp: ', s_temp)

        count += 1
        # print(i)
        if count1 == len(s):
            max_len = count
            print('max len: ', max_len)
    else:        
        print('s_temp in!!!!: ', s_temp)
        s_temp = s_temp[s_temp.index(i):]
        print('s_temp in!!!!: ', s_temp)

        
        # print('s_temp: ', s_temp)
        s_temp += i
        l = len(s_temp)
        
        
        # print('length: ',l)
        # count -= 1
        
        if max_len < count:
            max_len = count
            # print('max len: ', max_len)
            count = 0
        

print(max_len)



# for j in range(0, len(s)):
#     count1 += 1
#     for i in s:          
#         if i not in s_temp:
#             s_temp += i
#             count += 1
#             # print(i)
#             if count1 == len(s):
#                 max_len = count
#         else:
#             s_temp = i
#             if count > max_len:
#                 max_len = count
#                 count = 1
    
  


print('max len: ', max_len)
print('count1: ', count1)


# for i in s:
#     count1 += 1
   
#     if chr(ord(i)) not in s_temp:
#         s_temp += chr(ord(i))
#         count += 1
#     else:
#         s_temp = chr(ord(i))
#         if count > max_len:
#             max_len = count
#             count = 1




# print('max len: ', max_len)
# print('count1: ', count1)




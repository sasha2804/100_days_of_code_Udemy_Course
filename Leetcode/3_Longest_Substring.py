s = "abcabcbb"
# s = "ua"
# s='pwwkew'
# s = "dvdfg"
# s = ' '
# s = "pwwkew"
# s = 'abba'
# s = '    '
s = "jbpnbwwd"
# s = ' '


ls_temp = []
s_temp = ''
max_len = 0


if len(s) == 1:
    s *= 2

for i in s:
    for j in s:
        if j not in s_temp:
            s_temp += j            
        else:
            ls_temp.append(s_temp)            
            if len(s_temp) > max_len:
                max_len = len(s_temp)
            s_temp = ''
            break
    s = s[1:]

print(ls_temp)
print(max_len)


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         char_set = set()
#         max_len, start = 0, 0
#         for i, c in enumerate(s):
#             while c in char_set:
#                 char_set.remove(s[start])
#                 start += 1
#             char_set.add(c)
#             max_len = max(max_len, i - start + 1)
#         return max_len





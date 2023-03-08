class Solution:
     def isValid(self, strng):
         open_lst = ['(', '[', '{']
         close_lst = [')', ']', '}']
         stack = []

         if len(strng)%2 != 0:
             return False

         for i in strng:
            if i in open_lst:
                stack.append(i)
            elif i in close_lst:
                pos = close_lst.index(i)
                if len(stack) != 0 and open_lst[pos] == stack[-1]:
                    stack.pop()
                    # print(stack)                
                else:
                    return False         
         if len(stack) == 0:
             return True
         return False

s = "(("
# s = "()[()]{)}"
# s = "(]"

p_test = Solution()

print(p_test.isValid(s))
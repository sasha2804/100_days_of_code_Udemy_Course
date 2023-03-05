# x = '2'
# y = '3'

# for i in x:
#     print(i)
    


# class Solution:
#     def twoSum(self, nums, target):
#         for i in range(0, len(nums)):
#             for j in range(0, len(nums)):
#                 if i != j:
#                     s = nums[i] + nums[j]
#                     if s == target:
#                         return([i, j])               
  


# test = Solution()

# nums = [3,2,4]
# target = 6

# nums = [2,7,11,15]
# target = 9

# test.twoSum(nums, target)

# print(test.twoSum(nums, target))


'''
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

# nums = [2,7,11,15]
# target = 9

# for i in range(0, len(nums)-1):
#     for j in range(0, len(nums)-1):
#         if i != j:
#             s = nums[i] + nums[j]
#             if s == target:
#                 print([i, j])               
#     break

# class Solution:
#     def twoSum(self, nums, target):
#         for i in range(0, len(nums)-1):
#             for j in range(0, len(nums)-1):
#                 if i != j:
#                     s = nums[i] + nums[j]
#                     if s == target:
#                         return([i, j])       



# class Solution:

#     def isPalindrome(self, x):
#         rev_x = (str(x)[::-1])        
#         if rev_x == str(x):
#             return True
#         return False

#         # print(rev_x)


# is_palindrome = Solution()

# print(is_palindrome.isPalindrome(121))


from tkinter import S


# s = "MCMXCIV"
# s = "MCMXCIV"
s = "LVIII"
# s = "III"
# s = "MMMIIX"

'''
https://www.rapidtables.com/convert/number/roman-numerals-converter.html?x1=MXXXXVVX&x2=
'''

dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}



class Solution:
    def romanToInt(self, roman_num):
        trig = 0
        lst = []
        lst_final = []
        result = 0
        
        dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        for i in range(0, len(roman_num)):            
            x = dict[roman_num[i]]
            lst.append(x)              
        while len(lst) != 0:
            if len(lst) == 1 and trig == 0:
                lst_final.append(list[0])
                lst.pop(0)
                break
            if len(lst) == 1 and trig == 1:
                if lst[0] > lst_final[-1]/2:
                    lst_final.clear()
                else:
                    lst_final[-1] += lst[0]
                    lst.pop(0)
                break
            if lst[0] > lst[1]:
                lst_final.append(lst[0])
                lst.pop(0)
            elif lst[0] < lst[1]:
                
                if lst[1]/2 == lst[0]:
                    lst_final.clear()
                    break
                
                lst_final.append(lst[1] - lst[0])
                lst.pop(0)
                lst.pop(0)
            elif lst[0] == lst[1]:
                lst_final.append(lst[0] + lst[1])
                lst.pop(0)
                lst.pop(0)
                trig = 1
        # print(type(sum(lst_final)))
        # 
        print(type(lst_final[0]))

        print(lst_final)
        print(sum(lst_final))        
        
        if len(lst_final) != 0:        
            for j in (lst_final):
                result += j
                print(type(result))          
            return(result)
        return None


    


text_class = Solution()
# text_class(s)

print(text_class.romanToInt(s))


# x = '2'
# y = '3'

# for i in x:
#     print(i)
    


class Solution:
    def twoSum(self, nums, target):
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if i != j:
                    s = nums[i] + nums[j]
                    if s == target:
                        return([i, j])               
  


test = Solution()

nums = [3,2,4]
target = 6

# nums = [2,7,11,15]
# target = 9

test.twoSum(nums, target)

print(test.twoSum(nums, target))


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



class Solution:
    # def removeDuplicates(self, nums: List[int]) -> int:
    def removeDuplicates(self, nums):

        ret = []

        for i in nums:
            if i not in ret:
                ret.append(i)
            else:
                ret.append("_")
        
        nums = ret
        k = len(nums)
        # return  'nums=nums)


test = Solution()



lst = [1,1,2]


print(test.removeDuplicates(lst))




# Input: 
l1 = [2,4,3]
l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

class Solution:
    # def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    def addTwoNumbers(self, list1, list2):
        list_out = [list1, list2]
        sum_fin = 0
        sum_int = ''

        for list_in in list_out:
            list_in.reverse()
            list_in = [str(i) for i in list_in]           
            for i in list_in:
                sum_int += i  
            sum_fin += int(sum_int)
            sum_int = ''        
 

        sum_fin = list(str(sum_fin).strip())
        sum_fin.reverse()

        for i in range(len(sum_fin)):
            sum_fin[i] = int(sum_fin[i])             

        

        return(sum_fin)



solution = Solution()


print((solution.addTwoNumbers(l1, l2)))
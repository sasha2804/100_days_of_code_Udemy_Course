# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    def mergeTwoLists(self, list1, list2):
        ret_lst = []

        print(list1)

        # while list1.next != None:
        #     print('test')       

        # # for i in range(0, len(list1)):
        #     first = list1[i].val
        #     second = list2[i].val          

        #     if first > second:
        #         first, second = second, first

        #     ret_lst.append(first)
        #     ret_lst.append(second)

        return ret_lst




node6 = ListNode(3,None)
node5 = ListNode(2,node6)
node4= ListNode(1,node5)




node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)

node1.next = node2
node2.next = node3



list1 = [node1, node2, node3]
list2 = [node4, node5, node6]

test = Solution()


print(test.mergeTwoLists(list1, list2))





        
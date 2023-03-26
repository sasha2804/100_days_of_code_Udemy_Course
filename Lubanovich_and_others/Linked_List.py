class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next



class LinkedList:

    def __init__(self):
        self.head = None
    
    def AddAtBegin(self, data):
        newNode = Node(data)
        newNode.next = self.head
        

    
    def PrintLinkedList(self):
        temp = self.head
        print('ok!!!!!!!!!!!!!!!!!!!')

        while temp.next:
            print(temp.val)
            temp = temp.next
            print('ok1231321')
        



       
testLL = LinkedList()

testLL.AddAtBegin(1)
testLL.AddAtBegin(2)
testLL.AddAtBegin(3)
testLL.PrintLinkedList()







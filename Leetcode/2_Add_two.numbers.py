class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next



class LinkedList:

    def __init__(self):
        self.head = None
    
    def AddAtBegin(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode.val
            print(self.head)
        
        newNode.next = self.head
        self.nead = newNode



        

    
    def PrintLinkedList(self):
        temp = self.head

        while temp:
            print(temp.val)
            temp = temp.next
        


testLL = LinkedList()


testLL.AddAtBegin(1)

testLL.PrintLinkedList()










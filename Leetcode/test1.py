# Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
# Create & Handle List operations
class LinkedList:
    def __init__(self):
        self.head = None
 
    # Method to display the list
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
 
    # Method to add element to list
    def addToList(self, newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return
 
        last = self.head
        # print('self.head: ',self.head)
        print('last1: ', last)
        while last.next:
            last = last.next

            print('last: ', last)
       
        last.next = newNode
 
        # # last.next = newNode

        # # last = self.head
        # # print('self.head: ',self.head)
        # # print('last: ', last)
        # while self.head.next:
        #     self.head = self.head.next
 
        # self.head.next = newNode


lst = LinkedList()


lst.addToList(1)
lst.addToList(2)
lst.addToList(3)

lst.printList()
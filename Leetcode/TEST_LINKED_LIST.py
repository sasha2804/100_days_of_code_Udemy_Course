class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList(Node):
    def __init__(self):
        self.head = None

    
    def addAtBegin(self, data):
        newNode = Node(data)

        newNode.next = self.head
        print('link: ', newNode.next)
        self.head = newNode
        print('head: ',self.head)


    def printLinkesList(self):
        last = self.head        
        while last.next != None:
            print(last.val)
            last = last.next
        print(last.val)

            

            



test = LinkedList()

test.addAtBegin(2)
test.addAtBegin(3)
test.addAtBegin(4)

test.printLinkesList()


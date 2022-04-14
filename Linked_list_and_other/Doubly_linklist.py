class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.pre = None

class Linklist:
    def __init__(self):
        self.head = None
        
    def printlist(self):
        # if self.head is None:
        #     print('no data')
        # else:
        #     temp = self.head
        #     while temp != None:
        #         print(temp.data, end=' ')

        #         temp = temp.next

        temp = self.head
        while temp!= None:
            print(temp.data,end=' ')
            
            temp = temp.next

    def InsertAtBeginning(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.head.pre = new_node
            new_node.next = self.head
            self.head = new_node

    def InseerAtEnd(self,data):
        new_node = Node(data)
        temp = self.head        

        if self.head is None:
            self.head = new_node
        else:
            while temp.next != None:
                temp = temp.next
            temp.next = new_node
            new_node.pre = temp
        
    def InsetAtPosition(self,position,data):
        new_node = Node(data)
        temp = self.head
        if position == 0:
            self.head = new_node
        for i in range(1,position):
            temp = temp.next

        new_node.pre = temp
        new_node.next = temp.next
        temp.next.pre = new_node
        temp.next = new_node

    def deleteNode(self,position):
        temp = self.head
        if temp is None:
            print('Element are not available')

        if position == 0:
            self.head = temp.next
            temp = None
            return

        else:
            for i in range(1,position-1):    # acording to normal numbering
            # for i in range(1,position):    #Acording to index
                temp = temp.next
            nextt = temp.next.next
            temp.next = None
            temp.next = nextt
            nextt.pre = temp

    def Sorting(self,head):
        current = head
        index = Node(None)
        if head is None:
            return
        else:
            while current is not None:
                index = current.next
                while index is not None:
                    if current.data > index.data:
                        current.data , index.data = index.data , current.data
                    index = index.next
                current = current.next

root = Linklist()
n1 = Node(5)
root.head = n1
n2 = Node(10)
n1.next = n2
n2.pre = n1
n3 = Node(30)
n2.next = n3
n3.pre = n2
print('without using any oother function tha list are')
root.printlist()
print()
root.InsertAtBeginning(40)
root.InseerAtEnd(12)
root.InsetAtPosition(1,14)      #index
print('The list is')
root.printlist()
print()
print('After the delete node the node is')
root.deleteNode(3)
root.printlist()
print('\nAfter the sorting the node is')
root.Sorting(root.head)
root.printlist()

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linklist:
    def __init__(self):
        self.head = None

    def InsertAtBeginning(self,new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def InsertAfter(self,prev_node,new_data):
        
        if prev_node is None:
            print('The given previous node must be linklist')
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

        # else:
        #     new_node = Node(new_data)
        #     temp = self.head

        #     for i in range(1,prev_node):
        #         temp = temp.next
        #     temp.next = new_node
        #     new_node.next = temp.next

    def InserAtEnd(self,new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node


    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data,end=' ')
            temp = temp.next
            
        # while self.head != 0:
        #     print(self.head.data, end=' ')

            # self.head = self.head.next

    def deletion(self,position):
        if self.head is None:
            print('Element are not available in the node')

        else:
            temp = self.head

            for i in range(1,position-1):
                temp = temp.next
            nextt = temp.next.next
            temp.next = nextt
            
            temp.next = None

    def Search(self,value):
        temp = self.head
        while temp is not None:
            if temp == value:
                return True
            temp = temp.next
        return False

llist = linklist()
# llist.printlist()

# llist.insertAtBeginning(3)
llist.head = Node(6)
n1 = Node(3)
n2 = Node(4)

llist.head.next = n1
n1.next = n2
llist.InsertAtBeginning(2)

# llist.InsertAtBeginning(4)
# llist.InserAtEnd(5)
# llist.InsertAfter(llist.head,10)
# llist.InsertAfter(1,10)
print('The list is')
llist.printlist()
print()
# print(llist.deletion(10))
# print(llist.Search(3))
# llist.printlist()
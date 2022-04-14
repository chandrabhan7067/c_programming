class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linklist:
    def __init__(self):
        self.head = None

    def Print_node(self):
        if self.head is None:
            print('No data is available')

        else:
            temp = self.head
            while temp.next != self.head:
                print(temp.data, end=' ')
                temp = temp.next
            print(temp.data)

        # while temp:
        #     print(temp.data)
        #     temp = temp.next
        #     if temp == self.head:
        #         break

    def InsetAtbeginning(self, new_data):
        new_node = Node(new_data)
        # temp = self.head
        # new_node.next = self.head

        if self.head is None:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
        new_node.next = self.head
        self.head = new_node

    def InsertAtPosition(self, position, new_data):
        new_node = Node(new_data)
        temp = self.head
        for i in range(1, position - 1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node


        # if temp.next != self.head:
        #     for temp in range(1,position-1):
        #             temp = temp.next
        #     new_node.next = temp.next
        #     temp.next = new_node
        #
        # else:
        #     new_node.next = self.head
        #     temp.next = new_node

    def InsetAtEnd(self,new_data):
        if self.head is None:
            new_node = Node(new_data)
            self.head = new_node
            new_node.next = self.head

        else:
            new_node = Node(new_data)
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def Deletion(self,posotion):
        temp = self.head
        if temp is None:
            print('Element are not available')

        else:
            for i in range(1,posotion-1):
                temp = temp.next
            temp.next = None
            temp.next = temp.next.next

root = Linklist()
root.InsetAtbeginning(10)
root.InsetAtbeginning(11)
root.InsetAtbeginning(12)
root.InsetAtbeginning(15)
root.InsertAtPosition(3,13)
root.InsetAtEnd(18)
root.Print_node()
# root.Deletion(3)
root.Print_node()
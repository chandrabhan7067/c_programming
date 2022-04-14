class Node:
    def __init__(self,parend):
        self.parend = parend
        self.left = None
        self.right = None

    def Insert(self,data):
        if self.parend:
            if data < self.parend:
                if self.left is None:
                   self.left = Node(data)
                else:
                   self.left.Insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.Insert(data)
        else:
            self.parend = data

    def print_node(self):
        print(self.parend)
        if self.left:
            self.left.print_node()
        if self.right:
            self.right.print_node()

ob = Node(10)
ob.Insert(4)
ob.Insert(2)
ob.Insert(1)
ob.Insert(5)
ob.print_node()
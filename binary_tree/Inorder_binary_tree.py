class Node:
    def __init__(self,parent):
        self.parent = parent
        self.left = None
        self.right = None
       
def Inorderd(data):
    if data:
       Inorderd(data.left)
       print(data.parent,">>-",end=' ')
       Inorderd(data.right)
    
    
def Preorder_traversal(Data):
    if Data:
        print(Data.parent,">>-",end=" ")   
        Preorder_traversal(Data.left)
        Preorder_traversal(Data.right)
        
def Postorder(Data):
    if Data:
        Postorder(Data.left)
        Postorder(Data.right)
        print(Data.parent,">>-",end=" ")


# ob = Node(3)
# ob.left =Node(4)
# ob.right = Node(5)
# ob.left.left =Node(1)
# ob.right.right =Node(8)
# ob.left.left.left =Node(7)
# ob.right.right.right =Node(6)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


print("inordered binary tree is")
Inorderd(root)
print()

print("Preordered binary tree is")
Preorder_traversal(root)
print()

print("Postordered binary tree is")
Preorder_traversal(root)
    
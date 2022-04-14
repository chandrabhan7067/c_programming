# # 8. Print complete Binary Search Tree (BST) in increasing order.

# class Node:
#     def __init__(self,parent):
#         self.parent = parent
#         self.left = None
#         self.right = None

# def Insert(node,Data):
#     if node is None:
#             return Node(Data)
        
#     elif Data<node.parent:
#         node.left = Insert(node.left,Data)

#     else:
#         node.right = Insert(node.right,Data)
        
#     return node
 
            
# def Inorder(data):
#     if data:
#         Inorder(data.left)
#         print(data.parent,"->",end=' ')
#         Inorder(data.right)
 
# root = Node(10)
# root.left = Node(10)
# root = Insert(root, 8)
# root = Insert(root, 3)
# root = Insert(root, 1)
# root = Insert(root, 6)
# root = Insert(root, 7)

# Inorder(root)
 
 
 
 
class Node:
    def __init__(self,parent):
        self.parent = parent
        self.left = None
        self.right = None
        
def insertion(node,data):
    if node is None:
        return Node(data)
    
    elif data<node.parent:
        node.left = insertion(node.left,data)

    else:
        node.right = insertion(node.right,data)

    return node

def inorder(root):
    if root:
        inorder(root.left)
        print(root.parent)
        inorder(root.right)

root = Node(4) 
root.left = Node(3)
root = insertion(root,10)
inorder(root)
class Node:
    def __init__(self,parent):
        self.parent = parent
        self.left = None
        self.right = None
        
def Search(node,value):
    if node is None: 
        return None
    
    elif node.parent == value:
        return node
    
    elif value < node.parent:
        return Search(node.left,value)
      
    else:
        return Search(node.right,value)
        
def Inorder(node):
    if node:
        Inorder(node.left)
        print(node.parent,'->',end=' ')
        Inorder(node.right)
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

Search(root,2)
  
Inorder(root)
class Node:
    def __init__(self,parent):
        self.parent = parent
        self.left = None
        self.right = None

  
def Min_value(node):
    current = node.left
    while(node.left is not None):
        current = current.left
    return current  

    
def Deletion(node,value):
    if node is None:
        return None
    
    if value<node.parent:
        node.left = Deletion(node.left,value)

    elif value>node.parent:
        node.right = Deletion(node.right,value)

    else:
        if node.left is None:
            temp = node.right
            node = None
            return temp
        
        elif node.right is None:
            temp = node.left
            node = None
            return temp
        
        temp =  Min_value(node.right)

        node.parent = temp.parent
        
        node.right = Deletion(node.right,temp.value)

    return node
 
   
def Insert(node,Data):
    if node is None:
            return Node(Data)
        
    elif Data<node.parent:
        node.left = Insert(node.left,Data)

    else:
        node.right = Insert(node.right,Data)
        
    return node
      
                       
def Inorder(data):
    if data:
        Inorder(data.left)
        print(data.parent,"->",end=' ')
        Inorder(data.right)
 
 
root = None
root = Insert(root, 8)
root = Insert(root, 3)
root = Insert(root, 1)
root = Insert(root, 6)
root = Insert(root, 7)
 
Deletion(root,61)
  
print("Inorder traversal: ", end=' ')
Inorder(root)
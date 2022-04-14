class node:
    def __init__(self,parent):
        self.parent = parent
        self.left = None
        self.right = None
        
def Complete(Data):
    if Data is None:
        return True

    if Data.left is None and Data.right is None:
        return True

    if Data.left is not None and Data.right is not None:
       return Complete(Data.left) and Complete(Data.right)
    
    if Data.left:
        return True

    return False

        
ob = node(10)
ob.left = node(9)
ob.left.left = node(9)
ob.right = node(6)
# ob.right.right = node(6)

if Complete(ob):
    print('Yes is a Complete binary tree')
else:
    print('It is not a omplete binary tree')
    
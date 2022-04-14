class Node:
    def __init__(self,parend):
        self.parend = parend
        self.left = None
        self.right = None

def Full_tree(data):
    if data is None:
        return True

    if data.left is None and data.right is None:
        return True

    if data.left is not None and data.right is not None:
        return Full_tree(data.left) and Full_tree(data.right)

    return False

ob = Node(3)
ob.left = Node(1)
ob.right = Node(7)
# ob.left.left = Node(5)

if Full_tree(ob):
    print('yes full')
else:
    print('not full')
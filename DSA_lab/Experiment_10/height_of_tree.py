# 10. Calculate the height of a binary tree.

class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def height(node):
    if node is None:
        return -1
    else:
        ldepth = height(node.left)
        rdepth = height(node.right)
        
        return max(ldepth,rdepth)+1
    
            
        #     3                           height is 0
        #    / \                          height is 1
        #   4   7
        #  / \
        # 1   8                           height is 2
    
root = Node(3)
root.left = Node(4)
root.right = Node(7)

root.left.left = Node(1)
root.left.right = Node(8)
# root.left.left.left = Node(1)
# root.right.right.right = Node(8)

# second = Node(8)
# third = Node(3)
# fourth = Node(1)
# fifth = Node(6)

# root.left.left = second
# second.left = fourth
# root.right.right = third
# third.right = fifth

print('Height is ',height(root))
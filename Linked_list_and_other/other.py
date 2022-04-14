# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.right = None
#         self.left = None

# def height(node):
#     llen = 0
#     rlen = 0
#     if node is None:
#         return 1
#     else:
#         llen = llen+1
#         height(node.left)
#         rlen = rlen+1
#         height(node.right)
#         return llen,rlen
#         # return max(ldepth,rdepth)+1
    
# root = Node(3)
# root.left = Node(4)
# root.right = Node(7)
# root.left.left = Node(4)
# root.right.right = Node(7)
# print(height(root))

for i in range(5):
    for j in range(5):
        for k in range(5):
            print([i][j])
            print([i][k])

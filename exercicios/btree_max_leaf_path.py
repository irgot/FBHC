from Node import Node
from collections import deque, defaultdict


# def max_leaf_path(root):
#     if(not root):
#         return -1*float('inf')
#     queue = deque()
#     queue.append(root)
#     max_leaf_path = 0
#     while queue:
#         current = queue.pop()
#         max_leaf_path += current.data
#         queue.append(current.left)
#         queue.append(current.right)
#         max_leaf_path += max(current.left, current.right)
#     return max_leaf_path


def max_leaf_pathR(root):
    if not root:
        return -1*float('inf')
    if(not root.left and not root.right):
        return root.data
    return (root.data + max(max_leaf_pathR(root.right), max_leaf_pathR(root.left)))


a = Node(5)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(2)
f = Node(12)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

# print(max_leaf_path(a))
print(max_leaf_pathR(a))

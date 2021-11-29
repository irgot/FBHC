from Node import Node
from collections import defaultdict, deque


def mintree(root):
    tree = deque()
    tree.append(root)
    if not root:
        return float('inf')
    minval = float('inf')
    while tree:
        current = tree.pop()
        if(current):
            minval = min(current.data, minval)
            tree.append(current.left)
            tree.append(current.right)
    return minval


def mintreeR(root):
    if root:
        return min(root.data, mintreeR(root.left), mintreeR(root.right))
    return float('inf')


a = Node(5)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(-15)
f = Node(12)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


print(mintree(a))
print(mintreeR(a))

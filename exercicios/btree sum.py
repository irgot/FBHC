from Node import Node
from collections import deque


def treeSum(root):
    if not root:
        return 0
    tree = deque()
    tree.append(root)
    sum_nodes = 0
    while tree:
        current = tree.popleft()
        if current:
            sum_nodes += current.data
            tree.append(current.left)
            tree.append(current.right)
    return sum_nodes


def treeSumR(root):
    if not root:
        return 0
    sum_data = root.data
    sum_data += treeSumR(root.left)
    sum_data += treeSumR(root.right)
    return sum_data


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
print(treeSum(a))
print(treeSumR(a))

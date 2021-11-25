from Node import Node
from collections import deque


def treeIncludes(root, target):
    if not root:
        return False
    queue = deque()
    queue.append(root)
    while queue:
        current = queue.popleft()
        if current.data == target:
            return True
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return False


def treeIncludesR(current, target):
    if not current:
        return False
    if current.data == target:
        return True
    return treeIncludesR(current.left, target) or treeIncludesR(current.right, target)


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
print(treeIncludesR(a, 'g'))

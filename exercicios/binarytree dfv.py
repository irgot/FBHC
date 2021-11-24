from collections import deque
from Node import Node


def dephFirstValues(root=None):
    if(not root):
        return ([])
    stack = list()
    stack.append(root)
    result = list()
    while stack:
        current = stack.pop()
        result.append(current.data)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return(result)


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


print(dephFirstValues(a))
print(dephFirstValues(None))

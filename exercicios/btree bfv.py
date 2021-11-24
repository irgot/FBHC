from Node import Node
from collections import deque


def breathFirstValues(root):
    if not root:
        return ([])
    stack = deque()
    stack.append(root)
    result = list()
    while stack:
        current = stack.popleft()
        result.append(current.data)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
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


print(breathFirstValues(a))
print(breathFirstValues(None))

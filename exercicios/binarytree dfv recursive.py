from Node import Node


def depthFirstValues(root):
    if(not root):
        return ([])
    leftData = list()
    rightData = list()
    rightData = depthFirstValues(root.right)
    leftData = depthFirstValues(root.left)
    return [root.data] + leftData + rightData


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


print(depthFirstValues(a))
print(depthFirstValues(None))

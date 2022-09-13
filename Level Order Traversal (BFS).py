from BST import print_tree

class node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

rt = node(1)
l,r = node(2), node(3)
ll , lr = node(4) , node(5)
rr = node(6)

rt.left = l
rt.right = r
l.left = ll
l.right = lr
r.right = rr


stack = [rt,None]

while len(stack) > 0 and stack!=[None]:
    root = stack[0]
    if root is not None:
        if root.left:stack.append(root.left)
        if root.right:stack.append(root.right)
        print(stack[0].value,end=" ")
        stack.pop(0)
    else:
        print(" ")
        stack.pop(0)
        stack.append(None)






































































































































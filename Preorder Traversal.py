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

def preorder_traversal(root):
    print(root.value , end=" ")
    if root.left:preorder_traversal(root.left)
    else:print(-1,end=" ")
    if root.right:preorder_traversal(root.right)
    else:print(-1,end=" ")

preorder_traversal(rt)
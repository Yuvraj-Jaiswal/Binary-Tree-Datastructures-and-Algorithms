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

def postorder_traversal(root):
    if root.left:postorder_traversal(root.left)
    if root.right:postorder_traversal(root.right)
    print(root.value,end=" ")

postorder_traversal(rt)
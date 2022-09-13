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

def sum_nodes(root):
    if root is None: return 0
    return sum_nodes(root.right)+sum_nodes(root.left)+1

print(sum_nodes(rt))
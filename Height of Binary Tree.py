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

def calculate_height(root,h = 0):
    if root is None: return h
    else:
        hl = calculate_height(root.left,h+1)
        hr = calculate_height(root.right, h+1)
        return max(hl,hr)

print(calculate_height(rt))
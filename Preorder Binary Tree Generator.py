from BST import print_tree

class node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

idx = -1
def build_tree(arr):
    global idx
    idx += 1
    if arr[idx]==-1 : return None
    new_node = node(arr[idx])
    new_node.left = build_tree(arr)
    new_node.right = build_tree(arr)
    return new_node

value = [1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]
r = build_tree(value)
print_tree(r)
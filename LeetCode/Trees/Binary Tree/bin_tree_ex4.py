class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert(root, key):
    if not root:
        return TreeNode(key)
    
    if key == root.val:
        return root

    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root

def inorder(root):
    if not root:
        return
    
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def minVal(root):
    while root and root.left:
        root = root.left
    
    return root

def remove(root, val):
    if not root:
        return None
    
    if val < root.val:
        root.left = remove(root.left, val)
    elif val > root.val:
        root.right = remove(root.right, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            minNode = minVal(root.right)
            root.val = minNode.val
            root.right = remove(root.right, minNode.val)
    
    return root


tree = TreeNode(10)


array = [6,3,1,2,15,14,13,12]

for n in array:
    tree = insert(tree, n)

inorder(tree)

remove(tree, 14)
print("------")
print("------")
print("------")
print("------")



inorder(tree)
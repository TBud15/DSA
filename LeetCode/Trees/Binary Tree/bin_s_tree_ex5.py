class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def insert(root, key):
    if not root:
        return TreeNode(key)
    
    if root.val == key:
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

def minValue(root):
    if not root:
        return None
    
    while root.left:
        root = root.left

    return root.val


def remove(root, key):
    if not root:
        return None
    
        
    if key < root.val:
        root.left = remove(root.left, key)
    elif key > root.val:
        root.right = remove(root.right, key)

    else:
        if root.left == None and root.right == None:
            return None
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        
        else:
            min_val = minValue(root.right)
            root.val = min_val
            root.right = remove(root.right, min_val)

    return root


    


tree = TreeNode(8)

tree = insert(tree, 7)
tree = insert(tree, 5)
tree = insert(tree, 3)
tree = insert(tree, 10)
tree = insert(tree, 12)
tree = insert(tree, 15)
    
tree = remove(tree, 15)

inorder(tree)

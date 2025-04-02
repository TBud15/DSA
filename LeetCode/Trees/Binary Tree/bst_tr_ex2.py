class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_to_bt(root, key):
    if not root:
        return TreeNode(key)

    if key < root.val:
        root.left = insert_to_bt(root.left, key)
    else:
        root.right = insert_to_bt(root.right, key)
    
    return root

def inorder(root):
    if not root:
        return None
    
    inorder(root.left)
    print(root.val)
    inorder(root.right)

tree = TreeNode()


tree = insert_to_bt(tree, 10)
tree = insert_to_bt(tree, 5)
tree = insert_to_bt(tree, 3)
tree = insert_to_bt(tree, 13)
tree = insert_to_bt(tree, 12)
tree = insert_to_bt(tree, 19)

inorder(tree)
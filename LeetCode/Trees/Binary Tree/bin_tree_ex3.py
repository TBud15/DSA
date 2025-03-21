class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self. left = left
        self.right = right


def insert_in_bt(root, key):
    if not root:
        return TreeNode(key)
    
    # if inserting key is the same as root value, return root in this case
    if key == root.val:
        return root

    # if inserting value is less than current root
    if key < root.val:
        root.left = insert_in_bt(root.left, key)
    else:
        root.right = insert_in_bt(root.right, key)
    
    return root

def inorder(root):
    if not root:
        return
    
    inorder(root.left)
    print(root.val)
    inorder(root.right)


tree = TreeNode(8)

array = [7,5,3,10,13,16,19]

# populating 
for n in array:
    tree = insert_in_bt(tree, n)

inorder(tree)
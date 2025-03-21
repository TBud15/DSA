class TreeNode:
    def __init__(self,val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

def insert(root, key):
    if root is None:
        return TreeNode(key)
    
    if root.val == key: # if we are trying to add key to the array, that already exists in our tree
        return root
    
    if root.val < key:
        root.right = insert(root.right, key) # recursive function
    else:
        root.left = insert(root.left, key) # recursive function
    
    return root
    
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

root = TreeNode(100)

insert(root, 20)
insert(root, 10)
insert(root, 30)
insert(root, 500)

inorder(root)
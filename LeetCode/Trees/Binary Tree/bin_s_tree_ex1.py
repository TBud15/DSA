class TreeNode:
    def __init__(self, data=None, leftNode=None, rightNode=None):
        self.data = data
        self.leftNode = leftNode
        self.rightNode = rightNode


def insert_in_tree(root, key):
    if root is None:
        return TreeNode(key)
    
    if root.data == key:
        return root
    
    if key < root.data:
        root.leftNode = insert_in_tree(root.leftNode, key)
    else:
        root.rightNode = insert_in_tree(root.rightNode, key)

    return root

def search_left_side(root):
    if root:
        search_left_side(root.leftNode)
        print(root.data)



root = None

root = insert_in_tree(root, 11)
root = insert_in_tree(root, 9)
root = insert_in_tree(root, 7)
root = insert_in_tree(root, 10)
root = insert_in_tree(root, 11)
root = insert_in_tree(root, 14)
root = insert_in_tree(root, 15)
root = insert_in_tree(root, 17)


def inorder_low_to_high(root):
    if not root:
        return
    inorder_low_to_high(root.leftNode)
    print(root.data)
    inorder_low_to_high(root.rightNode)

# inorder_low_to_high(root)

search_left_side(root)
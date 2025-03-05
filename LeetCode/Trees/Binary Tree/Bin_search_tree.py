# Node class
class TreeNode:
    def __init__(self,data, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right


# searching in binary search tree function

def search(root, target):
    if not root:
        return False
    
    if target > root.val:
        return search(root.right, target)
    elif target < root.val:
        return search(root.left, target)
    else:
        return True


# inserting nodes in is in BST(Binary search tree)

def insert(root, val):
    if not root:
        return TreeNode(val)

    if val > root.val:
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left, val)
    return root


# taking the minimum element from the binary tree

def minValueNode(root):
    curr = root

    while curr and curr.left:
        curr = curr.left
    return curr


# BST(Binary Search Tree) remove node

def minValueForRemove(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr

def remove(root, val):
    if not root:
        return None
    
    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            minNode = minValueForRemove(root.right)
            root.val = minNode.val
            root.right = remove(root.right, minNode.val)
    return root

def traversePrintLeft(root):
    curr = root
    while curr:
        print(curr.val)
        curr = curr.left

def traversePrintRight(root):
    curr = root
    while curr:
        print(curr.val)
        curr = curr.right



# create root node
root = TreeNode(50)

# insert elements
insert(root, 30)
insert(root, 70)
insert(root, 20)
insert(root, 40)
insert(root, 60)
insert(root, 80)

# print left and right side
print("Left side (decreasing):")
traversePrintLeft(root)
print("Right side (increasing):")
traversePrintRight(root)
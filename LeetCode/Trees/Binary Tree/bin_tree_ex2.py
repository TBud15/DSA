class TreeNode:
    def __init__(self,val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

array = []

    
def insert(root, key):
    if root is None:
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

def left_traverse(root):
    if not root:
        return
    while root:
        print(root.val)
        root = root.left

def right_traverse(root):
    if not root:
        return
    
    while root:
        print(root.val)
        root = root.right

def find_min(root):
    if not root:
        return
    
    while root.left:
        root = root.left
    print("Minimum root is: ", root.val)
    return root


# i should remove 3 from BST
def remove_key(root, key):
    if key == root.val:
        return
    
    if key < root.val:
        root.left = remove_key(root.left, key)
























tree = TreeNode(7)

tree = insert(tree, 7)
tree = insert(tree, 3)
tree = insert(tree, 2)

# inorder(tree) # transfered inorder binary search tree to list
print("---")

tree = insert(tree, 1)

tree = insert(tree, 15)
tree = insert(tree, 8)
tree = insert(tree, 19)
# inorder(tree)

left_traverse(tree)
# right_traverse(tree)
# find_min(tree)













































# implement binary search

# def binary_search(array):
#     inp = input("Please enter target integer: ")

#     try:
#         target = int(inp)
#     except ValueError:
#         print("That's not a valid integer. Please rerun the program and enter an integer.")
#         return

#     left, right = 0, len(array) - 1

#     while left < right:
#         middle = (left+right) // 2

#         if target < array[middle]:
#             right = middle - 1
#         elif target > array[middle]:
#             left = middle + 1
#         else:
#             print("Element found")
#             print("Index: ", middle)
#             return
        
#     print("Target: ", target, " --- not found")
            

# binary_search(array)
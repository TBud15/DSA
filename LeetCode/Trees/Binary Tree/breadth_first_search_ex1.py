from collections import deque

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

root = insert_in_tree(root, 4)
root = insert_in_tree(root, 3)
root = insert_in_tree(root, 2)
root = insert_in_tree(root, 6)
root = insert_in_tree(root, 5)
root = insert_in_tree(root, 7)

def bst(root):
    queue = deque()

    if root:
        queue.append(root)

    line = 0
    while len(queue) > 0:
        print("Level: ", line)
        for i in range(len(queue)):
            curr = queue.popleft()
            print(curr.data)
            if curr.leftNode:
                queue.append(curr.leftNode)
            if curr.rightNode:
                queue.append(curr.rightNode)
        line += 1

bst(root)
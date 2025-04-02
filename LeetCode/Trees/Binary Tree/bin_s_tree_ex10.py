from collections import deque

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


tree = TreeNode()

def bfs(root):
    queue = deque()

    if root:
        queue.append(root)
    
    level = 0
    while len(queue) > 0:
        print("Level: ", level)
        for _ in range(len(queue)):
            curr = queue.popleft()
            print(curr.val)

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        level += 1
    
root = None


root = insert(root, 4)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 6)
root = insert(root, 5)
root = insert(root, 7)


# inorder(tree)

bfs(root)    

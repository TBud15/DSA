from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Build the binary tree:
#         1
#       /   \
#      2     3
#     /     / \
#    4     5   6

def bfs(root):
    q = deque()

    if not root:
        return 0
    
    q.append(root)

    while q:
        level = []
        for _ in range(len(q)):
            key = q.popleft()
            level.append(str(key.val))

            if key.left:
                q.append(key.left)
            if key.right:
                q.append(key.right)
        print(" ".join(level))

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.right.left = TreeNode(5)
tree.right.right = TreeNode(6)

bfs(tree)
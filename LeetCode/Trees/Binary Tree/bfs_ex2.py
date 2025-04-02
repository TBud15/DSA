from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# tree = TreeNode(1)

# tree.left = TreeNode(2)
# tree.left.right = TreeNode(5)
# tree.right = TreeNode(3)
# tree.right.right = TreeNode(4)

def bfs(root):
    q = deque()
    if not root:
        return 0
    
    q.append(root)
    
    level = 0

    while q:
        for i in range(len(q)):
            curr = q.popleft()
            
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        
        level += 1

    return level

print(bfs())
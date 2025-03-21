class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Tree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_helper(self.root, key)
    
    # insert helper function
    def _insert_helper(self, root, key):
        if not root:
            return TreeNode(key)
        
        if key == root.val:
            print("Value already in the BST")
            return root
        
        if key < root.val:
            root.left = self._insert_helper(root.left, key)
        else:
            root.right = self._insert_helper(root.right, key)
        
        return root

    def inorder(self):
        root = self.root
        self._inorder_helper(root)

    # inorder helper function
    def _inorder_helper(self, root):
        if not root:
            return
        
        self._inorder_helper(root.left)
        print(root.val)
        self._inorder_helper(root.right)

    def search_for_target(self, key):
        found = self._search_for_target(self.root, key)

        if found:
            print(f"{key} is inside of a BST.")
        else:
            print(f"{key} not found in BST.")

    # search helper function
    def _search_for_target(self, root, key):
        if not root:
            return False
        
        if root.val == key:
            return True
        
        if key < root.val:
            return self._search_for_target(root.left, key)
        else:
            return self._search_for_target(root.right, key)

    

tree = Tree()

tree.insert(18)
tree.insert(10)
tree.insert(6)
tree.insert(15)
tree.insert(13)

# tree.inorder()

tree.search_for_target(13)
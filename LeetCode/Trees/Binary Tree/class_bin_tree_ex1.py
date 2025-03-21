class TreeNode:
    def __init__(self, value):
        self.value = value      # Value stored in the node
        self.left = None        # Left child (values less than this node)
        self.right = None       # Right child (values greater than this node)

    def __repr__(self):
        return f"TreeNode({self.value})"


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a new value into the BST using recursion."""
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """Recursive helper function to insert a value."""
        # Base case: found a spot for the new node.
        if node is None:
            return TreeNode(value)
        # If the value is less, insert into the left subtree.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        # If the value is greater, insert into the right subtree.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        # If the value is equal, do nothing to avoid duplicates.
        return node
    
    def inorder(self):
        self._inorder_traverse(self.root)
    
    def _inorder_traverse(self,root):
        if not root:
            return
        self._inorder_traverse(root.left)
        print(root.value)
        self._inorder_traverse(root.right)

bst = Tree()
values_to_insert = [50, 30, 70, 20, 40, 60, 80]

for n in values_to_insert:
    bst.insert(n)

bst.inorder()



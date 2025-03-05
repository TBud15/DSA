class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

    def __repr__(self):
        return str(self.value)


tree = Node(1, [Node(4, [Node(3), Node(7)]),
                Node(5),
                Node(2, [Node(6)])])

            
def traverse(node):
    print(node)
    for child in node.children:
        traverse(child)

def traverse_i(node):
    print("enter", node.value)
    for child in node.children:
        traverse(child)
    print("leave", node.value)

def count_nodes(node):
    result = 1
    
    for child in node.children:
        result += count_nodes(child)
    return result

print(count_nodes(tree))
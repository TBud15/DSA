class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_to_beg(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
    
    def add_to_end(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
        
        current_node.next = new_node
    
    def print_ll(self):
        if self.head is None:
            print("No nodes in linked list")
            return

        
        current_node = self.head

        while(current_node):
            print("Node: ", current_node.data)

            current_node = current_node.next
    

llist = LinkedList()

llist.add_to_beg("a")
llist.add_to_beg("b")

llist.add_to_end("k")
llist.add_to_end("a")

llist.print_ll()
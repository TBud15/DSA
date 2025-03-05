class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node

    
    def insert_at_end(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head

        while current_node.next:
            current_node = current_node.next
        
        current_node.next = new_node
    
    def print_ll(self):
        if self.head is None:
            print("No data in linked list")
        
        current_node = self.head

        while current_node:
            print("Node: ", current_node.data)
            current_node = current_node.next
        
        print("--- end of the linked list ---")
    
llist = LinkedList()

llist.insert_at_beg("e")
llist.insert_at_end("a")
llist.insert_at_end("k")
llist.print_ll()
        

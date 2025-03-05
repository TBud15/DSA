class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beggining(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        # O(n)
        current_node = self.head

        while(current_node.next):
            current_node = current_node.next
        
        current_node.next = new_node

    def print_ll(self):
        if self.head is None:
            print("No nodes")
        
        current_node = self.head
        print("-- List Started --")

        while (current_node):
            print("Node: ", current_node.val)
            current_node = current_node.next
        
        print(" -- List  Ended --")
            






llist = LinkedList()

llist.insert_at_beggining("a")
llist.insert_at_beggining("b")
llist.insert_at_end("c")
llist.insert_at_end("h")
llist.insert_at_end("g")

llist.print_ll()
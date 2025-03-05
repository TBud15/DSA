class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
    
    # insertion without keeping track of tail O(n) not O(1)
    def insert_at_end(self, data):
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
            print("There are no nodes to print")
            return
        
        current_node = self.head
        counter = -1

        while(current_node):
            counter += 1
            print(f"Node N:{counter}", current_node.value)
            current_node = current_node.next
            print("")
        
        print(" --- End of Linked List ---")
    

llist = LinkedList()

llist.insert_at_beginning("a")
llist.insert_at_end("e")
llist.insert_at_end("d")
llist.insert_at_end("f")
llist.insert_at_end("g")
llist.insert_at_end("x")
llist.insert_at_end("x")
llist.print_ll()
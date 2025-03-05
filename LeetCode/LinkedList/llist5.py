class Node:
    def __init__(self, data):
        self.val = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
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

        while(current_node.next):
            current_node = current_node.next
        
        current_node.next = new_node
    
    def print_ll(self):
        if self.head is None:
            print("No nodes to print")
            return

        current_node = self.head

        while (current_node):
            print("Node: ", current_node.val)
            current_node = current_node.next
        
        print("Linked list ended")


    def check_if_node_in_ll(self,data):
        if self.head is None:
            print("There it nothing to check, Linked List is empty")
            return
        
        current_node = self.head
        input_data = data

        while(current_node):
            if current_node.val == input_data:
                print(current_node.val, " is in Linked List")
                return
            else:
                current_node = current_node.next
        
        print("\n End of query, if no data above, then no value present in linked list. \n")

    def repoint_spec_node(self,data, change_data):
        if self.head is None:
            print("Linked list is empty")
            return
        
        to_change = data
        new_data = change_data

        current_node = self.head

        while(current_node):
            if current_node.val == to_change:
                current_node.val = new_data
                print("Node data changed")
                return
            current_node = current_node.next
        
        print("No specified value in Linked List.")


llist = LinkedList()

llist.insert_at_beginning("a")

llist.insert_at_end("k")
llist.insert_at_end("x")
llist.insert_at_end("n")

# llist.repoint_spec_node("a","x")

llist.print_ll()
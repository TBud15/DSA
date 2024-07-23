# Define a class for the Node
class Node:
    def __init__(self, data=None):
        self.data = data  # Assign data to the node
        self.next = None  # Initialize the next pointer as None

# Define a class for the Singly Linked List
class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list as None

    # Method to insert a node at the beginning of the list
    def insert_at_beginning(self, data):
        new_node = Node(data)  # Create a new node
        new_node.next = self.head  # Point the next of new node to current head
        self.head = new_node  # Update the head to be the new node

    # Method to insert a node at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)  # Create a new node
        if not self.head:  # If the list is empty
            self.head = new_node  # Make the new node the head
            return
        last_node = self.head  # Start from the head
        while last_node.next:  # Traverse to the end of the list
            last_node = last_node.next
        last_node.next = new_node  # Point the next of the last node to new node

    # Method to delete a node by key
    def delete_node(self, key):
        temp = self.head  # Start from the head
        if temp is not None:  # If the list is not empty
            if temp.data == key:  # If the head node itself holds the key
                self.head = temp.next  # Change the head to the next node
                temp = None  # Free the old head
                return
        while temp is not None:  # Otherwise, search for the key
            if temp.data == key:  # If the key is found
                break
            prev = temp  # Keep track of the previous node
            temp = temp.next  # Move to the next node
        if temp == None:  # If the key is not present in the list
            return
        prev.next = temp.next  # Unlink the node from the list
        temp = None  # Free the node

    # Method to search for a node by key
    def search(self, key):
        current = self.head  # Start from the head
        while current:  # Traverse the list
            if current.data == key:  # If the key is found
                return True  # Return True
            current = current.next  # Move to the next node
        return False  # Return False if the key is not found

linked_list = SinglyLinkedList()
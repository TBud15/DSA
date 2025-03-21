# correct edge cases

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_in_ll(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        current = self.head

        while current.next:
            current = current.next
        current.next = new_node

    def print_ll(self):
        if self.head is None:
            print("No linked list")
            return
        
        current = self.head

        while current:
            print(current.data)
            current = current.next
        
    # O(n)
    def search_in_ll(self, key):
        if self.head is None:
            print("No linked list")
            return
        
        current = self.head

        while current:
            if current.data == key:
                print(key, " is inside of a Linked List") 
                return
            current = current.next
        
        print("No such key found")

    
    def delete_element(self, key):
        if self.head is None:
            print("No linked list")
            return
        
        current = self.head

        while current:
            if current.next and current.next.data == key:
                if current.next.next:
                    current.next = current.next.next
                else:
                    self.remove_last_node()
            elif current.data == key:
                print("Element is first on linked list")
                self.head = current.next
                return
            else:
                current = current.next

    def remove_first_node(self):
        if self.head is None:
            print("No linked list")
            return
        
        if self.head.next:
            self.head = self.head.next
            return
        
    def remove_last_node(self):
        if self.head is None:
            print("No linked list")
            return
        
        current = self.head

        while current.next.next:
            current = current.next

        current.next = None

        

llist = LinkedList()

llist.insert_in_ll(2)
llist.insert_in_ll(7)
llist.insert_in_ll(12)
llist.insert_in_ll(83)
llist.insert_in_ll(41)

# llist.remove_first_node()
# llist.remove_last_node()

llist.delete_element(41)

# llist.search_in_ll(12)

llist.print_ll()
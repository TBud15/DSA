class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.selected = None
    
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
            print("No data in linked list to display")
            return
        
        current_node = self.head

        while(current_node):
            print(current_node.data)
            current_node = current_node.next
        
        print("--- End of the Linked List ---")
    
    def change_data_in_pointer(self, data):
        if self.head is None:
            print("No data in Linked List")
            return
        
        target = data

        current = self.head
        while current:
            if current.data == target:
                print("Location: ", current)
                print("Pointer data match: ", current.data)
                decision = True
                self.selected = current
                print("Pointer address saved to selected instance variable")
                
                
                while decision:
                    do_you_want = input("Do you want to exit program? ").lower()

                    if do_you_want == "yes":
                        return
                        
                    elif do_you_want == "no":
                        enter_new_data = input("Enter new data to search in Linked List: ")
                        llist.change_data_in_pointer(enter_new_data)
                    else:
                        print("hmm.. I didnt recognize this input, only yes or no is accepted")
                        continue
            
            current = current.next
        
        print("Pointer with specified data not found.")
    
    
        

    


llist = LinkedList()

llist.add_to_beg("second")
llist.add_to_beg("first")

llist.add_to_end("a")
llist.add_to_end("g")
llist.add_to_end("z")

llist.change_data_in_pointer("g")

direct_to_pointer = llist.selected
print("Pointer: ", llist.selected)
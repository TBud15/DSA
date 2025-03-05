class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None # pointer to the head
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node # point to ther first node
            return
        else:
            new_node.next = self.head # make new node point to the previous first node
            self.head = new_node # now update head pointer to the new_node just inserted to the beginning

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
        
        current_node.next = new_node

    def remove_first_node(self):
        if self.head is None:
            print("There are no nodes to remove")
            return
        
        self.head = self.head.next # move head of the node to the next node 

    def remove_last_node(self):
        if self.head is None:
            print("There are no nodes to remove")
            return
        
        if self.head.next is None:
            print("There is only one node in list, i will remove it")

            self.head = None
            return
        
        current = self.head
        while(current.next.next):
            current = current.next
        
        current.next = None

    def print_all_nodes(self):
        current_node = self.head

        while(current_node):
            print("-- ", current_node.data)
            current_node = current_node.next
        
        print("The next node is pointing to: ", current_node)
        
        print("--- End of linked list ---")



llist = LinkedList()

llist.insert_at_beginning("a")
llist.insert_at_end("b")

for i in range(10):
    llist.insert_at_end(i)

llist.insert_at_end("c")
llist.print_all_nodes()
        


    
    
    
    
    
    
    



    


# array = [1,2,3,3,4,5,5,6,6,7,7,8,8,10,13,15,17,23,27]



# def binary_search(array):
#     tr = int(input("Please enter target in array that you are searching: "))

#     low, high = 0, len(array) - 1

#     while low <= high:
#         medium = (low+high) // 2

#         if tr == array[medium]:
#             return True
        
#         elif tr < array[medium]:
#             high = medium - 1
#         else:
#             low = medium + 1
    
#     return -1

# result = binary_search(array)

# if result:
#     print("Target inside of inputed array")
# else:
#     print("Target is not inside array.")



# class Node:
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def insert_in_ll(self, key):
#         if not self.head:
#             self.head = Node(key)
#             print("No linked list to insert into, this is the first element inserted")
#             return
        
#         current = self.head 

#         while current.next:
#             current = current.next

#         current.next = Node(key)

#     def traverse(self):
#         if not self.head:
#             print("No Linked List to traverse through")
#             return
        
#         current = self.head

#         while current:
#             print(current.val)
#             current = current.next
        
#         print("--- End of Linked List ---")

#     def search_for_target(self, key):
#         if not self.head:
#             print("No linked list")
#             return
        
#         current = self.head
#         index = 0

#         while current:
#             if current.val == key:
#                 print("Target found: ", key)
#                 print("Iteration: ", index)
#                 return
            
#             current = current.next
#             index += 1
        
#         print("Value not inside of a Linked List.")
#         print("Value not found in ", index, " iterations")
#         return
    
#     def remove_value(self, key):
#         if not self.head:
#             print("No linked list")
#             return
        
#         if self.head.val == key:  # Handling removal of head node
#             self.head = self.head.next
#             return True
        
#         current = self.head
#         while current.next:
#             if current.next.val == key:
#                 current.next = current.next.next  # Skip the node with matching key
#                 return True
#             current = current.next

#         print("Value not found")

# llist = LinkedList()
# llist.insert_in_ll(10)    
# llist.insert_in_ll(15) 
# llist.insert_in_ll(19) 
# llist.insert_in_ll(25) 
# llist.insert_in_ll(34) 
# llist.insert_in_ll(54) 

# llist.remove_value(54)

# # llist.search_for_target(15)

# llist.traverse() 


# array = [42, 17, 93, 58, 29, 74, 11, 36, 88, 65, 50, 99, 5, 23, 81]


# def search(array, key):
#     if not array:
#         return None
    
#     hashmap = {}

#     for index, value in enumerate(array):
#         hashmap[value] = index

#     if key in hashmap:
#         print("Key is in the hashmap")
#         return key
    
#     return False


class StockPortfolio:
    def __init__(self):
        self.stockQ = 0
        self.profit = 0
        self.money_spend = 0

    def buy_order(self):
        self.stockQ += 1

    def stock_buy_trigger(self, target):
        stock_price = 0

        while True:
            if stock_price == target:
                print("Execute buy order")
                print("Stock bought on: ", stock_price)
                self.money_spend += target
                return
            else:
                print("Current Stock Price: ", stock_price)
                stock_price += 1


    def check_stock_quantity(self):
        print("Stock Quantity: ", self.stockQ)

    def total_money_spend(self):
        print("You spend total of: ", self.money_spend, "$")
        


def execute():
    stock = StockPortfolio()

    stock.stock_buy_trigger(5)

    stock.total_money_spend()


execute()


                

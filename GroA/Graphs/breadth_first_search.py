#Breadth First Search (BFS)
from collections import deque

#Hashmap, graph relationship
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def person_is_seller(name):
    return name[-1] == 'm'

def search_mango(name):
    search_queue = deque() # Creates a new queue
    search_queue += graph[name] #Adds all of your neighbors to the serach queue
    searched = [] #This array is how you keep track of which people you've searched before.

    while search_queue:
        person = search_queue.popleft() #grabs the first person off the queue
        if not person in searched: # Only search this person if you haven't already searched them.
            if person_is_seller(person): #Check if person is a mango seller
                print(person + " is a mango seller!") #yes, he is mango seller
                return True
            else:
                print(graph[person], " adding to the end of the queue")
                search_queue += graph[person] #No, they arent, add all of this person's friends to the search queue.
                searched.append(person) #Marks this person as searched
                print("Search Queue: ", search_queue)
                print("End of iteration -----")
    return False

search_mango("you")



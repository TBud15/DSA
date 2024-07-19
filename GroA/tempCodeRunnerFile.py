#Breadth First Search (BFS)
from collections import deque

#Hashmap for graph relationship
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def check_person(name):
    return name[-1] == 'm'

def find_mango(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        if name not in searched:
            check_name = search_queue.popleft()
            result = check_person(check_name)

            if result:
                print("We found mango, its in hands of ", check_name)
                return 
            else:
                search_queue += graph[check_name]
                searched.append(check_name)


find_mango("you")
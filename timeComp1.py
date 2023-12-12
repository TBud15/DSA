# # Example of O(1)
# array = [0,1,2,3,4]

# # retrieve the number found at index location 3 
# print(array[3]) 





# # Example of O(n)
# array = [0,1,2,3,4,5,6,7,8,9,10]

# if 5 in array:
#     print("five is still alive")








#Example of O(Log n)
array = [0,1,2,3,4,6,7,8,9,10]

print("##Step One")
print("Array")
print(array)
midpoint = int(len(array)/2)
print("the midpoint at step one is: " , array[midpoint])

print()

print("##Step Two")
array = array[:midpoint] # 6 is the midpoint of the array 
print("Array")
print(array)
# running this shows the numbers left to check 
# is 5 < 3 
# no 
# so discard the left hand side 

# so the array is halved again 
midpoint=int(len(array)/2)
print("the midpoint is: ",  array[midpoint])

print()
print("##Step Three") 
array = array[midpoint:] # so the array is halved at the midpoint
print(array)
# check for the midpoint 
midpoint=int(len(array)/2)
print("the midpoint is: " , array[midpoint])
# is 4 < 5 
# yes look to the right

print()
print("##Step Four") 
print(array[midpoint:]) 
# check for the midpoint 
array = array[midpoint:] # so the array is halved at the midpoint
midpoint=int(len(array)/2)



print()
print("##Step Five") 
array = array[midpoint:] 
print(array)
print("only one value to check and it is not 5")
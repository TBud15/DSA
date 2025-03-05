def binarySearch(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        middle = (low+high) // 2

        # check if target is present in the middle
        if arr[middle] == target:
            return middle
        
        # if target is greater, ignore left half
        elif arr[middle] < target:
            low = middle + 1

        #  if target is smaller then remove right side
        else:
            high = middle - 1
    
    # if we reach here then element was not present
    # in the array
    return -1

arr = [2,3,4,10,40]
target = 40

result = binarySearch(arr,target)

if result == -1:
    print("There are no such target in the array")
else:
    print("Target is at index: ", result) # prints index
    print("Target: ", arr[result]) # prints target
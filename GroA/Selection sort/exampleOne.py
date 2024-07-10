array = [5, 2, 3, 9, 18, 34, 98]

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    newArray = []

    for i in range(len(arr)):
        smallestNum = find_smallest(arr)
        newArray.append(arr.pop(smallestNum))
    return newArray

print(selection_sort(array))
#Output: [2, 3, 5, 9, 18, 34, 98]
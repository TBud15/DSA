def quicksort(array):
    if len(array) < 2:
        # Base case: arrays with 0 or 1 element are already sorted.
        return array
    else:
        # Recursive case: choose the first element as the pivot.
        pivot = array[0]
        # Sub-array of all the elements less than the pivot.
        less = [i for i in array[1:] if i <= pivot]
        # Sub-array of all the elements greater than the pivot.
        greater = [i for i in array[1:] if i > pivot]
        # Combine the sorted sub-arrays and the pivot.
        return quicksort(less) + [pivot] + quicksort(greater)

# Example usage:
print(quicksort([10, 5, 2, 3]))

#  Write out the code for the earlier sum function.

# def sum(array):
#     total = 0
#     for item in array: #Every item in array
#         total += item
#     return total

# array = [1,4,5,3,2,7]

# print(sum(array))


# Write a recursive function to count the number of items in a list

def count_items(lst):
    # Base case: if the list is empty, return 0
    if not lst:
        return 0
    # Recursive case: count the first item and add the count of the rest of the list
    else:
        return 1 + count_items(lst[1:])

# Example usage
example_list = [1, 2, 3, 4, 5]
print(count_items(example_list))  # Output: 5

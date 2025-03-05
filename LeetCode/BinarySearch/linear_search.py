from large_array import large_array
import time

array = large_array
target = 999999 # Searching for the smallest number (worst case for linear search)

def search_value(target):
    start_time = time.time()  # Start timing
    
    for n in array:
        if n == target:
            end_time = time.time()  # End timing
            print("Target found:", n)
            print("Time taken:", end_time - start_time, "seconds")
            return
    
    end_time = time.time()  # End timing for the "not found" case
    print("Target not found.")
    print("Time taken:", end_time - start_time, "seconds")

search_value(target)

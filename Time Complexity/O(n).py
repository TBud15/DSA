def process_list(arr):
    # Calculate the cumulative sum
    cumulative_sum = 0
    for num in arr:
        cumulative_sum += num

    # Find the maximum and minimum values
    max_value = max(arr)
    min_value = min(arr)

    # Reverse the list
    reversed_arr = arr[::-1]

    return {
        "cumulative_sum": cumulative_sum,
        "max_value": max_value,
        "min_value": min_value,
        "reversed_list": reversed_arr
    }

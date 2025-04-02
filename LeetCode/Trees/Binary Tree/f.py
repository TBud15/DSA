def two_sum(array, target):
    hashmap = {}

    for index, value in enumerate(array):
        diff = target - value 

        if diff in hashmap:
            return [index, hashmap[diff]]
        hashmap[value] = index
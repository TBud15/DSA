def twoSum(nums, target):
    sums = {}

    for i,n in enumerate(nums):
        diff = target - n
        if diff in sums:
            return (sums[diff], i)
        sums[n] = i
        print(sums) #prints dictionary after each iterate
    return

print(twoSum([6,4,12,3,4,7,2], 9))
# {6: 0}
# {6: 0, 4: 1}
# {6: 0, 4: 1, 12: 2}
# (0, 3)
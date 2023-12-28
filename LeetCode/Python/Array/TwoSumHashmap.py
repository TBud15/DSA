class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
    
    #This solution lies in its efficiency. It uses a single pass through the list (O(n) time complexity), making it much faster than a naive approach that checks all possible pairs.   
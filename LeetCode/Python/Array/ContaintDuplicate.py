class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set() #Use set data type for better time, dont use lists.
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
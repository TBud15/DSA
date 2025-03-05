# Given an array nums and an integer k, determine if there exist two equal elements within a window of size k.

nums = [1,2,7,3,3,3]
k = 3






















































# def findEqual(nums, k):
    
#     for L in range(len(nums)):
#         for R in range(L+1, min(len(nums), L + k)):
#             if nums[L] == nums[R]:
#                 return True
#     return False


# print(findEqual(nums, k))



















































# def checkArray(nums, k):

#     for L in range(len(nums)):
#         for R in range(L+1, min(len(nums), L + k)):
#             if nums[L] == nums[R]:
#                 return True
#     return False
        
# print(checkArray(nums,k))
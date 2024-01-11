class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {')' : '(', '}' : '{', ']': '['}

        for c in s:
            if c in hashMap:
                if stack and stack[-1] == hashMap[c]:
                    stack.pop()
                else:
                    return False
            else : 
                stack.append(c)

        return True if not stack else False


# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         hashMap = {')': '(', '}': '{', ']': '['}

#         for c in s:
#             if c in hashMap:
#                 # Use get method for safe retrieval and compare with popped item
#                 if stack and stack.pop() == hashMap.get(c):
#                     continue
#                 else:
#                     return False
#             else: 
#                 stack.append(c)

#         # Directly return the evaluation
#         return not stack

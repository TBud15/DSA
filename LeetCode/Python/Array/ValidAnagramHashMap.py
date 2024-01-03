class Solution:
    def bubble_sort(self, lst):
        n = len(lst)
        for i in range(n):
            for j in range(0, n-i-1):
                if lst[j] > lst[j+1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]
        return lst
    
    def isAnagram(self, s: str, t: str) -> bool:
        setA = list(s)
        setB = list(t)

        sortedA = self.bubble_sort(setA)
        sortedB = self.bubble_sort(setB)

        if sortedA == sortedB:
            return True
        return False
























# def isAnagram(s, t):
#     l1 = s
#     l2 = t
#     setA = []
#     setB = []

#     for i in l1:
#         setA.append(i)

#     for i in l2:
#         setB.append(i)

#     if setA == setB:
#         print("True")
#     else:
#         print("False")

#     print(setA)
        
# isAnagram("anagram","nagaram")

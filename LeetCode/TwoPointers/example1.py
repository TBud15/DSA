# Is palindrome problem

def isPalindrome(word):
    L, R = 0, len(word) -1 # setup L and R pointers, L in the beginning and R to the end of string
    while L < R: # while True(pointers does not intersect, then lopp)
        if word[L] != word[R]:
            return False
            L += 1 # move pointer right one digit
            R -= 1 # move pointer left one digit
    return True # if while loop exits, it means that every word[L] == word[R], that means palindrome


#Also given string, if same questions arrises, you can use syntatic sugar to save it to variable and then iterate with same algorithm as above.
s = "A man, a plan, a canal: Panama"

result = "".join([c.lower() for c in s if c.isalnum()]) # s is given string. It will save all this stirng into one, removing spaces and punctuation.
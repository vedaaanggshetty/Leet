class Solution(object):
    def isAnagram(self, s, t):
        
        char = [0] * 26
        for i in s:
            char[ord(i) - ord('a')]+=1
        
        for j in t:
            char[ord(j)- ord('a')]-= 1
        
        for k in char:
            if k != 0:
                return False
        return True
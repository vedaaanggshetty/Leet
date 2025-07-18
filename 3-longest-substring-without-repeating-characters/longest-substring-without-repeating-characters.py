class Solution(object):
    def lengthOfLongestSubstring(self, s):
        cSet = set()
        maxx = 0
        l = 0 
        for r in range(len(s)):
            while s[r] in cSet:
                cSet.remove(s[l])
                l += 1
            else:
                cSet.add(s[r])
            maxx = max(maxx, r - l + 1)
        return maxx
        

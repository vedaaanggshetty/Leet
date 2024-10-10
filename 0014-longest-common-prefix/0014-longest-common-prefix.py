class Solution(object):
    def longestCommonPrefix(self, strs):
        res = ""
        sortedS = sorted(strs)
        for i in range(len(sortedS[0])):
            for s in strs:
                if sortedS[0][i] != s[i] or len(s) == i:
                    return res
            res += sortedS[0][i]      
        return res
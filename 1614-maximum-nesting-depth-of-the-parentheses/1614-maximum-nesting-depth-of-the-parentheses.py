class Solution(object):
    def maxDepth(self, s):
        # st = []
        # top = -1
        curr = 0
        maxx = 0 
        for c in s:
            if c == "(":
                curr += 1
                maxx = max(maxx, curr)
            elif c == ")":
                curr -= 1
        return maxx
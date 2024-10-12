class Solution(object):
    def minSwaps(self, s):
        close = 0
        maxC = 0

        for c in s:
            if c == '[':
                close -= 1
            else:
                close += 1
            maxC = max(maxC, close)

        return(maxC + 1 )// 2
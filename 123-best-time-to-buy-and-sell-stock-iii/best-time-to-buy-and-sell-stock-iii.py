class Solution(object):
    def maxProfit(self, prices):
        A = -999999 
        B = float('-inf')
        C = float('-inf')
        D = float('-inf')

        for p in prices:
            A = max(A, -p)
            B = max(B, A + p)
            C = max(C, B - p)
            D = max(D, C + p)

        return D
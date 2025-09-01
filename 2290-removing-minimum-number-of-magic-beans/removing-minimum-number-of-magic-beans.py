class Solution(object):
    def minimumRemoval(self, beans):
        beans.sort()
        summ = sum(beans)
        n = len(beans)
        res = float('inf')
        for i, b in enumerate(beans):
            diff = summ - b * (n-i)
            res = min(res, diff)
        return res
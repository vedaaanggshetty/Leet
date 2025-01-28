class Solution(object):
    def sortedSquares(self, nums):
        sq = []
        for i in nums:
            sq.append(i**2)
        sorArr = sorted(sq)
        return sorArr
class Solution(object):
    def sortedSquares(self, nums):
        sq = [i ** 2 for i in nums]
        sortedArr = sorted(sq)
        return sortedArr
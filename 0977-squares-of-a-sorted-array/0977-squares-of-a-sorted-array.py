class Solution(object):
    def sortedSquares(self, nums):
        sq = []
        for i in nums:
            sq.append(i**2)
        sorArr = sorted(sq)
        return sorArr

    # else you can do
        # sq = [i**2 for i in nums]
        # sortedA = sorted(sq)
        # return sortedA
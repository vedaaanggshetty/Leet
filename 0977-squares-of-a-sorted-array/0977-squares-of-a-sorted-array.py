class Solution(object):
    def sortedSquares(self, nums):
        ans = collections.deque()
        l, r = 0, len(nums)-1
        while l<=r:
            left, right = abs(nums[l]), abs(nums[r])
            if left > right:
                ans.appendleft(left * left)
                l += 1
            else:
                ans.appendleft(right*right)
                r -= 1
        return list(ans)
        # sq = []
        # for i in nums:
        #     sq.append(i**2)
        # sorArr = sorted(sq)
        # return sorArr

    # else you can do
        # sq = [i**2 for i in nums]
        # sortedA = sorted(sq)
        # return sortedA
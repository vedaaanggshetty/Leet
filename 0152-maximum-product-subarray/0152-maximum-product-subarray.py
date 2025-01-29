class Solution(object):
    def maxProduct(self, nums):
        maxPro = 1
        res = nums[0]
        for n in nums:
            maxPro = max(n*maxPro,n)
            res = max(res, maxPro)
        return res
        
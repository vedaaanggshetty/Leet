class Solution:
    def maxProduct(self, nums):
        res = nums[0]
        n = len(nums)
        for i in range(n):
            p = nums[i]
            if p > res:
                res = p
            for j in range(i+1,n):
                p = p * nums[j]
                if p > res:
                    res = p
        return res
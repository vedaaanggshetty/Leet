class Solution:
    def maxProduct(self, nums):
        # for i in range(n):
        #     p = nums[i]
        #     if p > res:
        #         res = p
        #     for j in range(i+1,n):
        #         p = p * nums[j]
        #         if p > res:
        #             res = p
        # return res
        res = nums[0]
        n = len(nums)
        imax = res
        imin = res

        for i in range(1, n):
            
            if(nums[i] < 0):
                imax,imin = imin, imax
                
            imax = max(nums[i], imax * nums[i])
            imin = min(nums[i], imin * nums[i])

            res = max(res, imax)
        return res      
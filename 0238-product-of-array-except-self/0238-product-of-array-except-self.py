class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        new = [0] * n
        pre = 1

        for i in range(n):
            new[i] = pre
            pre = pre * nums[i]

        suff = 1
        for i in range(n-1, -1, -1):
            new[i] *= suff
            suff *= nums[i]

        return new
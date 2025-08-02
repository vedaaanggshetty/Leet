class Solution(object):
    def countWays(self, nums):
        n=len(nums)
        res=0
        nums.sort()
        if nums[0]>0:
            res+=1
        if nums[-1]<n:
            res+=1

        for i in range(n-1):
            s = i+1
            if nums[i]<s and nums[i+1]>s:
                res+=1
        return res

        # n = len(nums)
        # nums.sort()
        # res = 0
        # for i in range(n+1):
        #     c = sum(1 for num in nums if num < i)
        #     if c >= i and i not in nums:
        #         res += 1
        # return res
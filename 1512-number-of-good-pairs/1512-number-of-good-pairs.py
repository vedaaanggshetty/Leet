class Solution(object):
    def numIdenticalPairs(self, nums):
        n = len(nums)
        c= 0
        for i in range(n):
            for j in range(i+1, n):
                if(nums[i] == nums[j]):
                    # j += 1
                    c += 1
        return c
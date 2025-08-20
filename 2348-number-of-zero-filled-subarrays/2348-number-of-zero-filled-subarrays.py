class Solution(object):
    def zeroFilledSubarray(self, nums):
        # first simply add 1 zeroes count
        c  = 0 
        cons = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cons += 1
                c += cons
            else:
                cons = 0
        return c
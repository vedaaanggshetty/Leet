class Solution(object):
    def runningSum(self, nums):
        rSum = [nums[0]]
        for i in range(1, len(nums)):
            rSum.append(nums[i] + rSum[-1])
        return rSum
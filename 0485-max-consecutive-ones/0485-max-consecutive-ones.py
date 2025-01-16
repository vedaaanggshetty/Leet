class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        maxOne = 0
        for i in range(len(nums)):
            if nums[i]:
                count += 1
                maxOne = max(maxOne, count)
            else:
                count = 0
        return maxOne
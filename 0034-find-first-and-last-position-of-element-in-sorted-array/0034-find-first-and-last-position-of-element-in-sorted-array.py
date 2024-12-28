class Solution(object):
    def searchRange(self, nums, target):
        if target not in nums:
            return [-1,-1]
        
        start = nums.index(target)
        end = len(nums) - 1 - nums[::-1].index(target)

        return [start, end]

        
class Solution(object):
    def sortColors(self, nums):
        n = len(nums)
        for i in range(n):
            j = i
            while j>0 and nums[j-1] > nums[j]:
                nums[j],nums[j-1] = nums[j-1], nums[j]
                j -= 1
            
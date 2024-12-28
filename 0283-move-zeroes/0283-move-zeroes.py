class Solution(object):
    def moveZeroes(self, nums):
        notzero = 0
        n = len(nums)
        for i in range (n):
            if nums[i] != 0:
                nums[notzero], nums[i] = nums[i], nums[notzero]
                notzero += 1 
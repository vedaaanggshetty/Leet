class Solution(object):
    def findMin(self, nums):
        n = len(nums)
        for i in range(n):
            min = i
            for j in range(i+1, n):
                if nums[j] < nums[min]:
                    min = j
            nums[i],nums[min] = nums[min],nums[i]
        return nums[0]

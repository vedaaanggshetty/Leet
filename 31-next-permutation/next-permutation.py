class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)

        def isSort(arr):
            return arr == sorted(arr, reverse = True)
        
        if isSort(nums):
            nums.sort()
            return nums

        i = n - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i] , nums[j] = nums[j], nums[i]

        nums[i+1:] = reversed(nums[i+1:])
        return nums
        
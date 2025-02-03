class Solution(object):
    def nextPermutation(self, nums):
    # ill make an index pointer fromm last
        #  check for decreasing element from last
    # intuition is to replace the decreasing element with the next larger elemtn and reverse the array
        n = len(nums)
        j = n - 2
        if n < 2:
            return nums
        while j >= 0 and nums[j] >= nums[j+1]:
            j -= 1
        
        if j >= 0:
            i = n -1
            #  if decreasing swap else decrement piinter i
            while (nums[j] >= nums[i]):
                i -= 1
            nums[j], nums[i] = nums[i], nums[j]
        
        nums[j+1:] = reversed(nums[j+1:])
        return nums
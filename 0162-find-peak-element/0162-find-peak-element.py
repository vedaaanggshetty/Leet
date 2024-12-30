class Solution(object):
    def findPeakElement(self, nums):
        l = 0
        r = len(nums) - 1
     
        while l <= r:
            m = l+((r-l) // 2)
            #left greater
            if nums[m] < nums[m-1] and m>0:
                r = m-1
            elif m < len(nums)-1 and nums[m] < nums[m+1]:
                l = m+1
            else:
                return m



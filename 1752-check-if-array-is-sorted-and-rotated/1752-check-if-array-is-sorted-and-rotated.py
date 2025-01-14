class Solution(object):
    def check(self, nums):
        # check if it is in ascending order
        count = 0
        n = len(nums)
        for i in range(1,n):
            if nums[i-1] > nums[i]:
                count += 1
        # 
        for i in range(1,n):
            if num[n-1] > nums[0]:
                count += 1
        
        # return true if violations are less than or equal to 1
        return count <= 1
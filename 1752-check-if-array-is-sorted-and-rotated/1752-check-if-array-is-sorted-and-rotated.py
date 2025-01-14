class Solution(object):
    def check(self, nums):
        # check if it is in ascending order
        count = 0
        n = len(nums)
        for i in range(1,n):
            if nums[i-1] > nums[i]:
                count += 1
        # check if last element is grete thwn the first element
        if nums[n-1] > nums[0]:
            count += 1
        
        # return true if violations are less than or equal to 1
        return count <= 1

        # -------------- another approach ----------------
        # for i in range(1, n):
            # if (nums[i] > (nums[i+1] %n)):
                # count += 1
                # return count <= 1
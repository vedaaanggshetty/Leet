class Solution(object):
    def rearrangeArray(self, nums):
        a,b = 0,1
        n = len(nums)
        arr = [0] * n
        for i in range (n):
            if(nums[i] > 0):
                arr[a] = nums[i]
                a += 2
            if(nums[i] < 0):
                arr[b] = nums[i]
                b += 2
            i += 1
        return arr

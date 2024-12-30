class Solution(object):
    def rearrangeArray(self, nums):
        i,a,b = 0,0,1
        n = len(nums)
        arr = [0] * n
        while i <= n:
            if(a<n and nums[i] > 0):
                arr[a] = nums[i]
                a += 2
            if(b<n and nums[i] < 0):
                arr[b] = nums[i]
                b += 2
            i += 1
        return arr

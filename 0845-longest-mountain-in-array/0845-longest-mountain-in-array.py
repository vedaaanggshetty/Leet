class Solution(object):
    def longestMountain(self, arr):
        res = 0
        n = len(arr)
        # if n < 3:
        #     return 0
        
        for i in range(1,n-1):
            if arr[i-1] < arr[i] > arr[i+1]:
                l=r=i
                while l>0 and arr[l-1] < arr[l]:
                    l -= 1
                while r<n-1 and arr[r+1] < arr[r]:
                    r += 1
                res = max(res, r-l+1)
        
        return res

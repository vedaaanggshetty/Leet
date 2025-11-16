class Solution(object):
    def findClosestElements(self, arr, k, x):
        r = len(arr)-1
        l = 0

        while (r - l + 1) > k:
            if abs(arr[l] - x) > abs(arr[r] - x):
                l += 1
            else:
                r -= 1

        return arr[l:r+1]
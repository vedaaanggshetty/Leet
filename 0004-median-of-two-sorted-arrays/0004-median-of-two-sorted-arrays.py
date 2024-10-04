class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merge = sorted(nums1 + nums2)
        n = len(merge)
        if n % 2 == 0:
            #integer division using (//)
            med = (merge[n//2] + merge[n//2 - 1]) / 2.0
        elif n % 2 !=  0:
            med = merge[(n//2)]
        
        return med
        

class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
    
     res = (
        set(nums1).intersection(nums2) |
        set(nums1).intersection(nums3) |
        set(nums2).intersection(nums3)
         )
     return list(res)
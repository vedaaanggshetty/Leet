class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # bitwise and -> smaller value 
        # the largest value should came out with max& max
        # find the longest sub string only contain max value
        max_val = max(nums)
        count = 0
        max_len = 1
        for i in nums:
            if i == max_val:
                count += 1
            else:
                count = 0
            max_len = max(max_len, count)
        return max_len
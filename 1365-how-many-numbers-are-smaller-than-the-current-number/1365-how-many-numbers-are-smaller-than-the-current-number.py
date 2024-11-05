class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for num in nums:
            count = sum(1 for x in nums if x < num)
            result.append(count)
        return result

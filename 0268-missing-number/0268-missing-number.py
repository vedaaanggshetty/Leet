class Solution(object):
    def missingNumber(self, nums):
        # for i, v in enumerate(nums):
        #     if (i == v):
        #         return v+len(nums)
        #     else:
        #         return v-1
        return sum(range(len(nums)+1)) - sum(nums)
from collections import defaultdict

class Solution(object):
    def maximumSubarraySum(self, nums, k):
        count = defaultdict(int)
        curr_sum = 0
        max_sum = 0
        l = 0

        for r in range(len(nums)):
            count[nums[r]] += 1
            curr_sum += nums[r]

            if r - l + 1 > k:
                count[nums[l]] -= 1
                curr_sum -= nums[l]
                if count[nums[l]] == 0:
                    del count[nums[l]]
                l += 1

            if r - l + 1 == k and len(count) == k:
                max_sum = max(max_sum, curr_sum)

        return max_sum

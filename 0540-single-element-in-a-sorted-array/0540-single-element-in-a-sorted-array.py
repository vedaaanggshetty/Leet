class Solution(object):
    def singleNonDuplicate(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if m % 2 == 1:
                m -= 1  # Make m even, because pairs always start from an even index

            if nums[m] == nums[m + 1]:
                l = m + 2  # Move to the right half
            else:
                r = m  # Move to the left half (the answer is on the left side)

        # When l == r, we have found the unique element
        return nums[l]

class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        # boundary check for k > n --- 3 % 7 = 3
            # slice the last k elements  + first k elements
        nums[:] = nums[-k:] + nums[:-k]
        return nums
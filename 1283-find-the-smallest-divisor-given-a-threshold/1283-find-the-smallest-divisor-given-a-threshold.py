class Solution(object):
    def smallestDivisor(self, nums, threshold):
        # helper function
        def compute(d):
            return sum((n + d -1)//d for n in nums)

        l, r = 1, max(nums)
        while l < r:
            # mid = (l - (l+r//2)) 
            mid = (l + r)//2
            if compute(mid) > threshold:
                l = mid + 1
            else:
                r = mid
        return l
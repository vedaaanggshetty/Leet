class Solution(object):
    def searchRange(self, nums, target):
        def ge(x):
            lo = 0

            hi = len(nums)
            while lo < hi:
                mid = ( lo + hi ) // 2
                if nums[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        
        def gt(x):
            lo = 0
            hi = len(nums)
            while lo < hi:
                mid = ( lo + hi ) // 2
                if nums[mid] <= x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        left = ge(target)
        if left == len(nums) or nums[left] != target:
            return [-1,-1]
        
        right = gt(target) - 1
        return [left, right]

class Solution(object):
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)
        def canFinish(k):
            time = 0
            for pile in piles:
                time += (pile + k - 1) // k
            return time <= h
        
        while left < right:
            mid = (left + right) // 2
            if canFinish(mid):
                right = mid
            else:
                left = mid + 1
        return left
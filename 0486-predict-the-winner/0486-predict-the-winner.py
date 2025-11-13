class Solution(object):
    def predictTheWinner(self, nums):
        # n = len(nums)
        # dp = [[0] * n for _ in range(n)]
        
        # # check it at one point?
        # for i in range(n):
        #     dp[i][i] = nums[i]

        # for l in range(2, n+1):
        #     for i in range(n - l + 1):
        #         j = i + l - 1
        #         I = nums[i] - dp[i+1][j]
        #         J = nums[j] - dp[i][j-1]
        #         dp[i][j] = max(I, J)

        # return dp[0][n-1] >= 0

        # '''using LRU cache ?'''
        # N = len(nums)
        # lru = [[False] * N for _ in range(N+1)]
        # cache = [[0] * N for _ in range(N+1)]

        # def score(left, right):
        #     if left < right:
        #         return 0

        #     if lru[left][right]:
        #         return cache[left][right]
             
        #     l = nums[left] - score(left + 1, right)
        #     r = nums[right] - score(left, right - 1)
            
        #     lru[left][right] = True
        #     cache[left][right] = max(l, r)
        #     return cache[left][right]
        # return score(0, N-1) >= 0
        def helper(left, right):
            if left == right:
                return nums[left]
            return max(nums[left] - helper(left + 1, right), nums[right] - helper(left, right - 1))
        return helper(0, len(nums) - 1) >= 0
        
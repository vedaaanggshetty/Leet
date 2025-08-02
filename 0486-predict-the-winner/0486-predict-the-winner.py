class Solution(object):
    def predictTheWinner(self, nums):
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        
        # check it at one point?
        for i in range(n):
            dp[i][i] = nums[i]

        for l in range(2, n+1):
            for i in range(n - l + 1):
                j = i + l - 1
                I = nums[i] - dp[i+1][j]
                J = nums[j] - dp[i][j-1]
                dp[i][j] = max(I, J)

        return dp[0][n-1] >= 0
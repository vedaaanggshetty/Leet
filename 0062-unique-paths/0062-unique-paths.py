class Solution(object):
    def uniquePaths(self, m, n):
        ''' so you have to use dp here
            #1 without directions ( memoisation )
        '''
        dp = [[0] * n for _ in range (m)]
        for i in range(m):
            for j in range(n):

                if(i == 0 or j == 0):
                    dp[i][j] = 1
            
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]
class Solution(object):
    def countSquares(self, matrix):    
        count = 0
        # from collections import deque
        # visit = set()
        
        # lenth of matrix dims
        col = len(matrix[0])
        row = len(matrix)
    # ill use dp :)

        dp = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 1:
                    # check for 1's nearbty
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    count += dp[i][j]
        return count
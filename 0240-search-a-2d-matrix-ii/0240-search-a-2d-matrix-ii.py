class Solution(object):
    def searchMatrix(self, matrix, target):
        # brute force approach

        # cant use binary search because row and column arent contiguously arranged in ascending order
        row = len(matrix)
        col = len(matrix[0])

        i = row - 1
        j = 0

        while j<col and i >= 0:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                j += 1
            else: 
                i -= 1
        return False

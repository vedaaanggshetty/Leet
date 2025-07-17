class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        col = len(matrix[0])
        l = 0 
        r = row * col - 1
        while l <= r:
            m = (l + r) // 2
            mVal = matrix[m // col][m % col]
            
            if mVal == target:
                return True
            
            elif mVal < target:
                l = m + 1
            else:
                r = m - 1
        return False
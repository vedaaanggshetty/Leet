class Solution(object):
    def rotate(self, matrix):
    #    row = [matrix[i] for i in range(len(matrix))]
    #    col = [matrix[j][i] for j in range(len(matrix))]
        for i in range(len(matrix)):
           for j in range(i, len(matrix)):
              matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(len(matrix)):
            matrix[i].reverse()
















        #    row = matrix[i]
        #    col = [matrix[j][i] for j in range(len(matrix))]

        # newMatrix = []
        
        # row[i]
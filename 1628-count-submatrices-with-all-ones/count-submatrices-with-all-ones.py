class Solution(object):
    def numSubmat(self, mat):
        m, n = len(mat), len(mat[0])
        heights = [0] * n
        total = 0

        for i in range(m):
            # update histogram heights
            for j in range(n):
                if mat[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0

            # count submatrices ending at row i
            for j in range(n):
                if heights[j] == 0:
                    continue
                min_h = heights[j]
                for k in range(j, -1, -1):
                    if heights[k] == 0:
                        break
                    min_h = min(min_h, heights[k])
                    total += min_h
        return total

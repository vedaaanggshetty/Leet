class Solution(object):
    def sortMatrix(self, grid):
        # threshold 
        # check if (i - j) for all diags
        #  if i >=0 then under and inckiding diag
        #  else above
        from collections import defaultdict
        n = len(grid)
        diag = defaultdict(list)

        for i in range(n):
            for j in range(n):
                diag[i-j].append(grid[i][j])

        for k in diag:
            if k >= 0:
                diag[k].sort(reverse = True)
            else:
                diag[k].sort()
            
        for i in range(n):
            for j in range(n):
                grid[i][j] = diag[i-j].pop(0)

        return grid

        
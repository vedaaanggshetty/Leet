from collections import defaultdict
class Solution(object):
    def isValidSudoku(self, board):
        row = defaultdict(set)
        col = defaultdict(set)
        sqr = defaultdict(set)

        # iterate thru the grid
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if (val in row[r] 
                or val in col[c] 
                or val in sqr[(r//3 , c//3)]):
                    return False            
                # if cond
                if val == ".":
                    continue
                # something here
                col[c].add(val)
                row[r].add(val)
                sqr[(r//3, c//3)].add(val)
        return True
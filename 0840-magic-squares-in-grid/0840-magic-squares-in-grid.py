class Solution(object):
    def numMagicSquaresInside(self, grid):
        magicc = self.gen()
        row = len(grid)
        col = len(grid[0])
        c = 0
        for i in range(row - 2):
            for j in range(col - 2):
                sub = [row[j:j+3] for row in grid[i:i+3]]
                if sub in magicc:
                    c += 1
        return c
    # first check for the combinations of magic grid 
    # one base case then twist and turn it ( trans + rotate )
    
    @staticmethod
    def reflect(square):
        return [r[::-1] for r in square]
    
    @staticmethod
    def rotate(square):
        return [list(r) for r in zip(*square[::-1])]

    def gen(self):
        base = [[4,3,8],[9,5,1],[2,7,6]]
        magic = []
        curr = base

        for _ in range(4):
            magic.append(curr)
            magic.append(self.reflect(curr))
            curr = self.rotate(curr)

        return magic
    
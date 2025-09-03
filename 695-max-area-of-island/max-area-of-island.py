class Solution(object):
    def maxAreaOfIsland(self, grid):
        if not grid:
            return 0
        maxx = 0
        que = collections.deque()

        row = len(grid)
        col = len(grid[0])
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    area = 0
                    que.append((r,c))
                    grid[r][c] = 0

                    while que:
                        r,c = que.popleft()
                        area += 1
                        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                            nr, nc = r + dr, c + dc

                            if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                                grid[nr][nc] = 0
                                que.append((nr,nc))
                    maxx = max(maxx,area)
        return maxx        

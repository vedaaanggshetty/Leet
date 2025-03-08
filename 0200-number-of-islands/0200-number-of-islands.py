class Solution(object):
    def numIslands(self, grid):
        def bfs(r,c):
            q = deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                dir = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in dir:
                    r,c = dr+row, dc+col
                    if(r in range(rows) and c in range(cols) and grid[r][c] == '1' and (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))


        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        co = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visit:
                    bfs(r,c)
                    co += 1
        return co
class Solution(object):
    def orangesRotting(self, grid):
        # 2 rotten
        # 1 fresh, 0 no
        
        que = collections.deque()
        # is it right to start from 2 ?
        row = len(grid)
        col = len(grid[0])
        fresh = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    que.append((r,c,0))
                elif grid[r][c] == 1:
                    fresh += 1
        minutes = 0
        
        # then  BFS to whatever is `1?`
        while que:
            r, c, minn = que.popleft()
            minutes = max(minutes, minn)

            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0<= nc < col and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    que.append((nr,nc, minn + 1))

        return minutes if fresh == 0 else -1

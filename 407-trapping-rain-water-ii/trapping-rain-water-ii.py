class Solution(object):
    def trapRainWater(self, heightMap):
        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3:
            return 0

        # Step 1: initialize water levels
        water = [[float('inf')] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    water[i][j] = heightMap[i][j]

        changed = True
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        # Step 2: relax until stable
        while changed:
            changed = False
            for i in range(1, m-1):
                for j in range(1, n-1):
                    minNeighbor = min(water[i+di][j+dj] for di,dj in dirs)
                    newLevel = max(heightMap[i][j], minNeighbor)
                    if newLevel < water[i][j]:
                        water[i][j] = newLevel
                        changed = True

        # Step 3: compute trapped water
        total = 0
        for i in range(m):
            for j in range(n):
                total += water[i][j] - heightMap[i][j]
        return total

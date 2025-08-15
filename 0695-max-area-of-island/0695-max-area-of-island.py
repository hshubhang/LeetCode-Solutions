class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        visited = [[False for c in range(cols)]for r in range(rows)]
        def dfs(i, j):
            areacount = 0
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0 or visited[i][j]:
                return 0
            visited[i][j] = True
            areacount = 1
            areacount += dfs(i-1, j)
            areacount += dfs(i+1, j)
            areacount += dfs(i, j - 1)
            areacount += dfs(i, j+1)

            return areacount

        area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and not visited[r][c]:
                    areacount = dfs(r, c)
                    area = max(area, areacount)
        return area

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        row = len(grid)
        cols = len(grid[0])
        count = 0
        visited = [[False for j in range(cols)] for i in range(row)]
        def dfs(i, j):
            area_count = 0
            if (i < 0 or i >= row or 
                j < 0 or j >= cols or 
                visited[i][j] or 
                grid[i][j] == 0
            ):
                return 0
            visited[i][j] = True
            area_count = 1
        
            area_count += dfs(i + 1, j)
            area_count += dfs(i, j + 1)
            area_count += dfs(i - 1, j)
            area_count += dfs(i, j - 1)
        
            return area_count
        max_area = 0
        for i in range(row):
            for j in range(cols):
                if grid[i][j] == 1 and not visited[i][j]:
                    area = dfs(i, j)
                    max_area = max(max_area, area)

        return max_area
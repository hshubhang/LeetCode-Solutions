class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])

        visited = [[False for c in range(cols)]for r in range(rows)]

        def dfs(i, j):
            perimeter = 0
            if i < 0 or i >= rows or j < 0 or j >= cols or grid [i][j] == 0:
                return 1
            if visited[i][j]:
                return 0
            
            visited[i][j] = True
            perimeter += dfs(i - 1, j)
            perimeter += dfs(i+1, j)
            perimeter += dfs(i, j-1)
            perimeter += dfs(i, j + 1)

            return perimeter

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and not visited[r][c]:
                    perimeter = dfs(r,c) 

        return perimeter
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        visited = [[False for j in range(cols)] for i in range(rows)]

        counter = 0
        def dfs (i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == "0" or visited[i][j] == True:
                return
            
            visited[i][j] = True

            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i, j - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and not visited[r][c]:
                    dfs(r,c)
                    counter += 1

        return counter
        


        



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        visited = [[False for c in range(cols)]for r in range(rows)]

        def bfs(i, j):
            q = deque()
            q.append((i,j))
            visited[i][j] = True

            while q:
                row, col = q.popleft()

                for dr, dc in [(-1, 0), (1, 0), (0, -1),(0, 1)]:
                    nr = row + dr
                    nc = col + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and not visited[nr][nc]:
                        visited[nr][nc] = True
                        q.append((nr, nc))
                        
            
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and not visited[r][c]:
                    bfs(r, c)
                    islands += 1

        return islands
        



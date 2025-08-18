class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for c in range(cols)]for r in range(rows)]
        if grid[0][0] != 0 or grid[rows - 1][cols - 1] != 0:
            return -1
        queue = deque([(0, 0, 1)])
        visited[0][0] = True
        directions = [(-1,0),(1,0),(0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]
        while queue:
            row, col, dist = queue.popleft()
            if row == rows - 1 and col == cols - 1:
                return dist
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == 0:
                    queue.append((nr, nc, dist + 1))
                    visited[nr][nc] = True


        return -1
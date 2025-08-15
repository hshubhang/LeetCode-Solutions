class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        rows = len(grid)
        cols = len(grid[0])

        visited = [[False for c in range(cols)]for r in range(rows)]
        directions = [(-1,0), (1,0), (0, -1), (0, 1)]
        queue = deque()
        fresh = 0
        time = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and not visited[r][c]:
                    fresh += 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visited[r][c] = True

        while queue:
            infected_this_minute = False
            layer_size = len(queue)
            for _ in range(layer_size):

                row, col = queue.popleft()
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
                        infected_this_minute = True
                        visited[nr][nc] = True
            if infected_this_minute:
                time += 1

        return time if fresh == 0 else -1
 
            

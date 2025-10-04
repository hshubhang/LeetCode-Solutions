class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        if not maze:
            return -1

        rows = len(maze)
        cols = len(maze[0])

        entrance_row, entrance_col = entrance

        visited = [[False for c in range(cols)] for r in range(rows)]
        directions = [(-1,0), (1,0), (0, -1), (0, 1)]
        queue = deque([(entrance_row, entrance_col, 0)])
        visited[entrance_row][entrance_col] = 1

        while queue:

            r, c, steps = queue.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
            
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == "." and not visited[nr][nc]:
                    if nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1:
                        return steps + 1

                    visited[nr][nc] = True
                    queue.append((nr, nc, steps + 1))
        
        return -1


            


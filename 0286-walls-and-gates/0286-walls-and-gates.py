class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        rows = len(rooms)
        cols = len(rooms[0])

        visited = [[False for c in range(cols)]for r in range(rows)]
        queue = deque()
        inf = 2147483647
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c, 0))
                    visited[r][c] = True

        while queue:
            row, col, distance = queue.popleft()

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and rooms[nr][nc] == inf :
                    rooms[nr][nc] = distance + 1
                    visited[nr][nc] = True
                    queue.append((nr, nc, distance + 1))

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return []
        rows = len(image)
        cols = len(image[0])
        visited = [[False for c in range(cols)]for r in range(rows)]
        queue = deque()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue.append((sr, sc))
        visited[sr][sc] = True
        
        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and image[nr][nc] == image[sr][sc]:
                    image[nr][nc] = color
                    queue.append((nr, nc))
                    visited[nr][nc] = True

        image[sr][sc] = color
        return image
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        pq = []
        row, col = len(heights), len(heights[0])
        effort_to = [[inf] * col for _ in range(row)]
        effort_to[0][0] = 0

        pq = [(0, 0, 0)]
        heapq.heapify(pq)
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        visited = [[False] * col for _ in range(row)]


        while pq:
            
            effort, r, c = heapq.heappop(pq)
            visited[r][c] = True

            if r == row - 1 and c == col - 1:
                return effort

            for dr, dc in directions:

                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and not visited[nr][nc]:
                    current_diff = abs(heights[nr][nc] - heights[r][c])
                    new_effort = max(effort, current_diff)

                    if new_effort < effort_to[nr][nc]:
                        effort_to[nr][nc] = new_effort
                        heapq.heappush(pq, (new_effort, nr, nc))




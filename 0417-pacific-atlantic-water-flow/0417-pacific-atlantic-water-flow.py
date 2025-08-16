class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        res = []
        rows = len(heights)
        cols = len(heights[0])
        directions = [(-1, 0), (1, 0), (0,-1), (0, 1)]
        visited_pac = [[False for c in range(cols)] for r in range(rows)]
        visited_atl = [[False for c in range(cols)] for r in range(rows)]


        def dfs(i, j, visited):
            visited[i][j] = True

            for dr, dc in directions:
                nr, nc = i + dr, j + dc
            
                if (0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and heights[nr][nc] >= heights[i][j]):
                    dfs(nr, nc, visited)

            
        for c in range(cols):
            if not visited_pac[0][c]:
                dfs(0, c, visited_pac)
            if not visited_atl[rows - 1][c]:
                dfs(rows - 1, c, visited_atl)

        for r in range(rows):
            if not visited_pac[r][0]:
                dfs(r, 0, visited_pac)
            if not visited_atl[r][cols - 1]:
                dfs(r, cols - 1, visited_atl)

        res = []

        for r in range(rows):
            for c in range(cols):
                if visited_pac[r][c] and visited_atl[r][c]:
                    res.append([r, c])
        
        return res
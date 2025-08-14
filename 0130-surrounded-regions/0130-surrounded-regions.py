class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        
        rows = len(board)
        cols = len(board[0])

        visited = [[False for c in range(cols)] for r in range(rows)]

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] == "X" or visited[i][j]:
                return

            visited[i][j] = True
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)


        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[rows - 1][c] == "O":
                dfs(rows-1, c)
        
        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][cols - 1] == "O":
                dfs(r, cols - 1)
            
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and not visited[r][c]:
                    board[r][c] = "X"
        

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        n = len(board)

        columns = list(range(0, n))

        cells = [None] * (n**2 + 1)
        label = 1
        for row in range(n-1, -1 ,-1):
            for column in columns:
                cells[label] = (row,column)
                label += 1
            columns.reverse()
        distance = [-1] * (n**2 + 1)
        queue = deque([1])
        distance[1] = 0
        while queue:
            curr = queue.popleft()
            for next in range(curr + 1, min(curr + 6, n**2) + 1):
                row, column = cells[next]
                destination = (board[row][column] if board[row][column] != -1 else next)
                if distance[destination] == -1:
                    distance[destination] = distance[curr] + 1

                    queue.append(destination)

        return distance[n * n]

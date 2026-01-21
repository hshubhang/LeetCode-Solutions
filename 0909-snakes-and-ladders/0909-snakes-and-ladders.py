class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        n = len(board)
        columns = list(range(0, n))
        cells = [None] * (n**2 + 1)
        label = 1
        for row in range(n-1, -1, -1):
            for column in columns:
                cells[label] = board[row][column]
                label += 1
            columns.reverse()

        queue = deque([1]) 
        visited = {1}
        moves = 0
        
        while queue:

            for level in range(len(queue)):

                curr = queue.popleft()

                if curr == n * n:
                    return moves

                for roll in range(curr + 1, min(curr + 6, n**2) + 1):

                    if cells[roll] != -1:
                        roll = cells[roll]

                    if roll not in visited:
                        visited.add(roll)
                        queue.append(roll)
                    
            moves += 1

        
        return -1

            


        print(cells)

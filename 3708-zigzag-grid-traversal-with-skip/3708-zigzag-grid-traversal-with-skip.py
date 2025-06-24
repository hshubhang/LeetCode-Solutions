class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        
        ans = []
        row = len(grid)
        col = len(grid[0])

        for r in range(row):
            if r % 2 == 0:
                col_range = range(0, col)
                for c in col_range:
                    if c % 2 == 0:
                        ans.append(grid[r][c])
            else:
                col_range = range(col -1, -1, -1)
                for c in col_range:
                    if c % 2 != 0:
                        ans.append(grid[r][c])


        return ans


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        count = 0
        rowmap = defaultdict(int)

        for i in range(r):
            row_arr = []
            for j in range(c):
                row_arr.append(grid[i][j])

            rowmap[tuple(row_arr)] += 1
        colmap = defaultdict(int)
        for i in range(c):
            col_arr = []
            for j in range(r):
                col_arr.append(grid[j][i])

            count += rowmap[tuple(col_arr)]


        return count




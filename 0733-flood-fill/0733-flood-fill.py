class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old = image[sr][sc]
        if old == color:
            return image
        rows = len(image)
        cols = len(image[0])

        visited = [[False for c in range(cols)] for r in range(rows)]


        def dfs(i, j, color):

            if i < 0 or i >= rows or j < 0 or j >= cols or visited[i][j] or image[i][j] != old:
                return

            visited[i][j] = True
            image[i][j] = color

            dfs(i-1, j, color)
            dfs(i+1, j , color)
            dfs(i, j-1, color)
            dfs(i, j+1, color)



        dfs(sr, sc, color)

        return image

        
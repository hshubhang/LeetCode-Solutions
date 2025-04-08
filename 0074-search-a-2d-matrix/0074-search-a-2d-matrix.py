class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:       
            m = len(matrix)
            n = len(matrix[0])

            first , last = 0, (m*n - 1)

            while first <= last:
                mid = first + (last - first) // 2

                rows = mid // n
                cols = mid % n
                if matrix[rows][cols] == target:
                    return True
                elif matrix[rows][cols] < target:
                    first = mid + 1
                else:
                    last = mid - 1

            return False
                




class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        count = 0

        if not citations:
            return 0

        left = 0
        right = len(citations)

        while left < right:

            mid = (left + right) // 2

            remaining = n - mid

            if citations[mid] >= remaining:
                right = mid
            else:
                left = mid + 1
                

        
        return n - left

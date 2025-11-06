class Solution:
    def hIndex(self, citations: List[int]) -> int:
        max_count = 0
        n = len(citations)
        if not citations:
            return 0
        
        citations.sort()


        for i in range(n):
            remaining = n - i

            if citations[i] >= n - i:
                max_count = max(max_count, remaining)

        
        return max_count



            



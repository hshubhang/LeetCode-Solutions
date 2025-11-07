class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        count = 0

        if not citations:
            return 0

        for i in range(n):
            remaining_papers = n - i

            if citations[i] >= remaining_papers:
                count = max(count, remaining_papers)
            
        
        return count


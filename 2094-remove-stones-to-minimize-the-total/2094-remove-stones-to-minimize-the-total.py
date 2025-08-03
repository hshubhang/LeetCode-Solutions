class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = [-pile for pile in piles]

        heapq.heapify(max_heap)

        for i in range(k):
            largest = abs(heapq.heappop(max_heap))
            heapq.heappush(max_heap, - (largest - floor(largest / 2)))

        return abs(sum(max_heap))



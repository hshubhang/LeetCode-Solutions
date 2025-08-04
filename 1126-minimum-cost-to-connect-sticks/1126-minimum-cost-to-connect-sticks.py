class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        min_heap = sticks
        heapq.heapify(min_heap)
        cost = 0
        while len(min_heap) > 1:
            first = heapq.heappop(min_heap)
            second = heapq.heappop(min_heap)
            new_stick = first + second
            heapq.heappush(min_heap, new_stick)
            cost += new_stick

        return cost
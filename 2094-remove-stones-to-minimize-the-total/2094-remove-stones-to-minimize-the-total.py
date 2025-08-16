class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        maxheap = [-pile for pile in piles]

        heapq.heapify(maxheap)

        for i in range(k):
            stone = heapq.heappop(maxheap)
            heapq.heappush(maxheap, floor(stone / 2))

        res = [-stone for stone in maxheap]

        return sum(res)


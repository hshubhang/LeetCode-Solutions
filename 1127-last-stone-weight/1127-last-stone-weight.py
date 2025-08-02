class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            biggest = abs(heapq.heappop(stones))
            second_biggest = abs(heapq.heappop(stones))

            if biggest != second_biggest:
                heapq.heappush(stones, -abs(biggest - second_biggest))
            else:
                continue

        return -stones[0] if stones else 0
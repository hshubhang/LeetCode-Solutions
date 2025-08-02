class Solution:
    def halveArray(self, nums: List[int]) -> int:
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        total = sum(nums)
        reduced = 0
        count = 0
        while reduced < total / 2:
            largest = -heapq.heappop(max_heap)
            half = largest / 2
            reduced += half
            heapq.heappush(max_heap, -half)
            count += 1

        return count


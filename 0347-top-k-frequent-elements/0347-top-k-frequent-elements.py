class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)

        for i in nums:
            if i not in hashmap:
                hashmap[i] = 0
            if i in hashmap:
                hashmap[i] += 1

        heap = []

        for num, frequency in hashmap.items():
            heapq.heappush(heap, (frequency, num))
            if len(heap) > k:
                heapq.heappop(heap)
            
        return [num for frequency, num in heap]

   
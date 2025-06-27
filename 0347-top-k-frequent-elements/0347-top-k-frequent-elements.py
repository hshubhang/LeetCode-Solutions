class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)

        for i in nums:
            if i not in hashmap:
                hashmap[i] = 0
            if i in hashmap:
                hashmap[i] += 1

        sorted_items = sorted(hashmap.items(), key=lambda item :item[1], reverse = True)
        return list(item[0] for item in sorted_items[:k])

   
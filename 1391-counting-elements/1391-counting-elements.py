class Solution:
    def countElements(self, arr: List[int]) -> int:
        hashmap = defaultdict(int)
        for num in arr:
            hashmap[num] = 0

        for i in arr:
            if i + 1 in hashmap:
                hashmap[i] += 1
        count_nonzero_keys = sum(value for value in hashmap.values() if value > 0)
        return count_nonzero_keys
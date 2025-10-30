class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        left = 0
        hashmap = defaultdict(int)
        length = float('inf')

        for right in range(len(cards)):
            hashmap[cards[right]] += 1

            while hashmap[cards[right]] > 1:
                hashmap[cards[left]] -= 1
                length = min(length, right - left + 1)
                left += 1
        return length if length != float('inf') else -1
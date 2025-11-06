class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        stones_count = Counter(stones)
        count = 0
        for i in jewels:
            if i in stones_count:
                count += stones_count[i]

        return count



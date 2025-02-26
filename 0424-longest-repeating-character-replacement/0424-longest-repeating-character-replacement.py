class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 1
        right = len(s) + 1

        while left + 1 < right:
            mid = left + (right - left) // 2

            if self.canMakeValidSubstring(s, mid, k):
                left = mid
            else:
                right = mid

        return left

    
    def canMakeValidSubstring(self, s: str, sub_string_length: int, k: int):
        hashmap = defaultdict(int)
        maxFreq = 0
        start = 0
        for end in range(len(s)):
            hashmap[s[end]] += 1

            if (end - start) + 1 > sub_string_length:
                hashmap[s[start]] -= 1
                start += 1
            maxFreq = max(maxFreq, hashmap[s[end]])
        if sub_string_length - maxFreq <= k:
            return True
    
        return False

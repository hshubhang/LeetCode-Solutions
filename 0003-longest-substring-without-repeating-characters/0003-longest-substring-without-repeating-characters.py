class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = max_count = 0
        hashmap = defaultdict(int)

        for right in range(len(s)):
            hashmap[s[right]] += 1

            while hashmap[s[right]] > 1:
                hashmap[s[left]] -= 1
                left += 1
            max_count = max(max_count, right - left + 1)

        return max_count

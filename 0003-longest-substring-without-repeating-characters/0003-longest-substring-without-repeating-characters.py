class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = defaultdict(int) 
        left = best = 0
        for right in range(len(s)):
            hashmap[s[right]] += 1
        
            while hashmap[s[right]] > 1:
                hashmap[s[left]] -= 1
                left+= 1
            best = max(best, right - left + 1)
        return best
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = defaultdict(int)  # Corrected defaultdict initialization
        left = best = 0  # No need for `curr`
        
        for right in range(len(s)):
            hashmap[s[right]] += 1
            
            while hashmap[s[right]] > 1:
                hashmap[s[left]] -= 1 
                left += 1 
            best = max(best, right - left + 1)
        
        return best

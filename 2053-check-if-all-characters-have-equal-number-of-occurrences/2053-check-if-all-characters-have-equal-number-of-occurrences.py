class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hashmap = defaultdict(int)
        for char in s:
            hashmap[char] += 1
        
        unqiue_vals = set(hashmap.values())
        if len(unqiue_vals) == 1:
            return True
        else:
            return False
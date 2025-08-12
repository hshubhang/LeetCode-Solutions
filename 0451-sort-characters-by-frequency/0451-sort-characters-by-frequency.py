class Solution:
    def frequencySort(self, s: str) -> str:
        
        list_s = list(s)

        frequency = Counter(list_s)

        sorted_chars = sorted(frequency.keys(), key= lambda ch: frequency[ch], reverse= True)

        return "".join(char * frequency[char] for char in sorted_chars)
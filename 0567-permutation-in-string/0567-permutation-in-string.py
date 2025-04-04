class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        input_frequency = Counter(s1)
        start, end = 0, len(s1)
        comparer_string = Counter(s2[start:end])
        for _ in range(len(s2)):
            if comparer_string == input_frequency:
                return True
            else:
                comparer_string = Counter(s2[start:end])
                end += 1
                start += 1
        
        return False

            
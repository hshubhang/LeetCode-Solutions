class Solution:
    def reverseString(self, s: List[str]) -> None:
        first = 0
        last = len(s) - 1
        while first <= last:
            temp = s[last]
            s[last] = s[first]
            s[first] = temp
            first += 1
            last -= 1
        
        return s
        
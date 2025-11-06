class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        count = 0
        left = 0
        right = 0

        while right <= len(chars) - 1:

            if chars[right] == chars[left]:
                count += 1
                right += 1
            elif chars[right] != chars[left]:
                if count == 1:
                    s += f"{chars[left]}"
                else:
                    s += f"{chars[left]}{count}" 
                left = right
                count = 0
            
        if count == 1:
            s += f"{chars[left]}"
        else:
            s += f"{chars[left]}{count}" 

        for i in range(len(s)):
            chars[i] = s[i]
        
        return len(s)
                

        
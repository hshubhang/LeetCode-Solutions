class Solution:
    def compress(self, chars: List[str]) -> int:
        s = []
        S = []
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
                    S.append(chars[left])
                else:
                    s += f"{chars[left]}{count}" 
                    S.append(chars[left])
                    S.append(str(count))
                left = right
                count = 0
            
        if count == 1:
            s += f"{chars[left]}"
            S.append(chars[left])
        else:
            s += f"{chars[left]}{count}" 
            S.append(chars[left])
            S.append(str(count))

        new_str = "".join(S)
        print(new_str)

        for i in range(len(new_str)):
            chars[i] = new_str[i]
        
        return len(s)
                

        
class Solution:
    def isValid(self, s: str) -> bool:
        split_string = list(s)
        stack = []
        mapping_dict = {")":"(", "}":"{", "]":"["}
        for i in split_string:
            if i in mapping_dict:
                if not stack:
                    return False
                top = stack.pop()
                if mapping_dict[i] != top:
                    return False
            else:
                stack.append(i)

        if stack:
            return False
        else:
            return True

        
        


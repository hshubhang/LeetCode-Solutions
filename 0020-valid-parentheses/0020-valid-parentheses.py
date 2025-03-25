class Solution:
    def isValid(self, s: str) -> bool:
        split_string = list(s)
        bracket_dict = {")":"(", "]":"[", "}":"{"}
        stack = []
        for i in split_string:
            if i not in bracket_dict:
                stack.append(i)
            elif stack and stack[-1] == bracket_dict[i]:
                stack.pop()
            else: 
                return False
        if stack:
            return False
        else:
            return True
        


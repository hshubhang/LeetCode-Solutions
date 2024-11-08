class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []

        for alphabet in s:
            if alphabet == "#" and not stack1:
                continue
            elif alphabet == "#" and stack1:
                stack1.pop()
            else:
                stack1.append(alphabet)
        for char in t:
            if char == "#" and not stack2:
                continue
            elif char == "#" and stack2:
                stack2.pop()
            else:
                stack2.append(char)
        
        if stack1 == stack2:
            return True

        return False
        
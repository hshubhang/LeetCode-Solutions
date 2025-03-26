class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for current in list(s):
            if stack and abs(ord(current) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(current)
        return "".join(stack)
        
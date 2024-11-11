class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for curr_alpha in list(s):
            if stack and abs(ord(curr_alpha) - ord(stack[-1]) ) == 32:
                stack.pop()
            else:
                stack.append(curr_alpha)
        return "".join(stack)

            
        
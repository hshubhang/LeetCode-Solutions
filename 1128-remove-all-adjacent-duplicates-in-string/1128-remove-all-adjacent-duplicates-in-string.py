class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for alphabet in s:
            if stack and stack[-1] == alphabet:
                stack.pop()
            else:
                stack.append(alphabet)
        return "".join(stack)
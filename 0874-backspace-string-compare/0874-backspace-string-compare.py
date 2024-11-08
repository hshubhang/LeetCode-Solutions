class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def build(s):
            stack1 = []

            for alphabet in s:
                if alphabet == "#" and not stack1:
                    continue
                elif alphabet == "#" and stack1:
                    stack1.pop()
                else:
                    stack1.append(alphabet)
            return "".join(stack1)
        return build(s) == build(t)
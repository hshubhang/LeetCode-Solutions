class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        curr_min = 0
    def push(self, val: int) -> None:
        self.stack.append(val)
        curr_min = val
        self.minstack.append(min(val, curr_min))

    def pop(self) -> None:
        del self.stack[-1]
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
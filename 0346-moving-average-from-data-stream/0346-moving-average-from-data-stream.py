from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.size = size
        

    def next(self, val: int) -> float:
        self.queue.append(val)

        if len(self.queue) > self.size:
            self.queue.popleft()
        
        avg = sum(self.queue) / len(self.queue)

    
        return avg
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
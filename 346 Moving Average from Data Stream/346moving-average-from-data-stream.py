class MovingAverage:

    def __init__(self, size: int):
        self.queue = collections.deque()
        self.cap = size
        self.total = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.total += val

        if len(self.queue) > self.cap:
            self.total -= self.queue.popleft()
        
        return self.total / len(self.queue)

# Time: O(1)
# Space: O(n)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
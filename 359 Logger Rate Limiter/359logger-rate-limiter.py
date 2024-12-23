class Logger:

    def __init__(self):
        self.time = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.time and self.time[message] + 10 > timestamp:
            return False
        self.time[message] = timestamp
        return True

# Time: O(1)
# Space: O(n)


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
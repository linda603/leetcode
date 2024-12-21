class tree:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
    
    def insert(self, startTime, endTime):
        curr = self

        while True:
            if endTime <= curr.start:
                if not curr.left:
                    curr.left = tree(startTime, endTime)
                    return True
                curr = curr.left
            elif startTime >= curr.end:
                if not curr.right:
                    curr.right = tree(startTime, endTime)
                    return True
                curr = curr.right
            else:
                return False

class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.root:
            self.root = tree(startTime, endTime)
            return True
        return self.root.insert(startTime, endTime)

# Time: O(logn) everage, O(n) worst time
# Space: O(n)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
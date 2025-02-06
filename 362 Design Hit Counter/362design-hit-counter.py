class HitCounter:

    def __init__(self):
        self.records = []

    def hit(self, timestamp: int) -> None:
        self.records.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        target = timestamp - 300
        l = 0
        r = len(self.records) - 1

        while l <= r:
            mid = (l + r) // 2
            if self.records[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return len(self.records) - l

# Time: getHits(): O(logn)
# Space: O(n)

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
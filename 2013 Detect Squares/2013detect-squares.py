class DetectSquares:

    def __init__(self):
        # do not name self.count as there is a count() API in this class
        self.freq = {}

    def add(self, point: List[int]) -> None:
        if tuple(point) not in self.freq:
            self.freq[tuple(point)] = 0
        self.freq[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        xp, yp = point
        res = 0

        for p, cnt in self.freq.items():
            x, y = p
            # p and query point need to be diagnal
            if x == xp or y == yp or (abs(x - xp) != abs(y - yp)):
                continue
            if (x, yp) in self.freq and (xp, y) in self.freq:
                res += cnt * self.freq[(x, yp)] * self.freq[(xp, y)]
        return res

# Time: add(): O(1), count: O(n)
# Space: O(n) due to self.freq

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
class Solution:

    def __init__(self, w: List[int]):
        self.weights = []
        self.total = 0

        for num in w:
            self.total += num
            self.weights.append(self.total)

    def pickIndex(self) -> int:
        target = random.random() * self.total
        res = 0

        l = 0
        r = len(self.weights) - 1

        while l <= r:
            mid = (l + r) // 2
            if self.weights[mid] >= target:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
        
# Time: constructor(): O(n), pickIndex(): O(logn)
# Space: O(n)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
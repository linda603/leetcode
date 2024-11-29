class MedianFinder:

    def __init__(self):
        self.max_heap = [] # smaller numbers
        self.min_heap = [] # larger numbers

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -1 * num)
        heapq.heappush(self.min_heap, -1 * heapq.heappop(self.max_heap))

        if len(self.min_heap) > len(self.max_heap) + 1:
            heapq.heappush(self.max_heap, -1 * heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if (len(self.max_heap) + len(self.min_heap)) % 2:
            return self.min_heap[0]
        return (-1 * self.max_heap[0] + self.min_heap[0]) / 2
        
# Time: addNum() O(logn). findMedian() O(1)
# Space: O(n)

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
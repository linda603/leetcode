class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.count = 0
        self.set = set()

    def popSmallest(self) -> int: #O (logn)
        if self.heap:
            curr = heapq.heappop(self.heap)
            self.set.remove(curr)
            return curr
        self.count += 1
        return self.count        

    def addBack(self, num: int) -> None: # O(logn)
        if num <= self.count and num not in self.set:
            heapq.heappush(self.heap, num)
            self.set.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

#Space: O(n) n: number of elements in heap
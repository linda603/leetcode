class Heap:
    def __init__(self):
        self.heap = [0]

    def push(self, val):
        i = len(self.heap)
        self.heap.append(val)

        # Percolate up
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2
    
    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()

        i = 1
        res = self.heap[1]
        # move the last value to the root
        self.heap[1] = self.heap.pop()

        # Percolate down
        while i * 2 < len(self.heap):
            # swap right child
            if i * 2 + 1 < len(self.heap) and self.heap[i * 2 + 1] < self.heap[i * 2] and self.heap[i * 2 + 1] < self.heap[i]:
                self.heap[i * 2 + 1], self.heap[i] = self.heap[i], self.heap[i * 2 + 1]
                i = i * 2 + 1
            elif self.heap[i * 2] < self.heap[i]:
                self.heap[i * 2], self.heap[i] = self.heap[i], self.heap[i * 2]
                i = i * 2
            else:
                break
        return res

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = Heap()
        self.k = k

        for num in nums:
            self.heap.push(num)
            if len(self.heap.heap) > k + 1:
                self.heap.pop()

    def add(self, val: int) -> int:
        self.heap.push(val)
        if len(self.heap.heap) > self.k + 1:
            self.heap.pop()
        print(self.heap.heap)
        
        return self.heap.heap[1]
        
# Time: constructor(): O(nlogk). add(): O(logk)
# Space: O(k)

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
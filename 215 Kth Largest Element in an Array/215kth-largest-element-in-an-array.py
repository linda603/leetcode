class Heap:
    def __init__(self):
        self.heap = [0]
    
    def push(self, val):
        i = len(self.heap)
        self.heap.append(val)

        # Percolate up
        while i // 2 and self.heap[i] < self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2
    
    def pop(self):
        res = self.heap[1]
        i = 1
        self.heap[1] = self.heap.pop()

        # Percolate down
        while i * 2 < len(self.heap):
            # Swap right child
            if i * 2 + 1 < len(self.heap) and self.heap[i * 2 + 1] < self.heap[i] and self.heap[i * 2 + 1] < self.heap[i * 2]:
                self.heap[i * 2  + 1], self.heap[i] = self.heap[i], self.heap[i * 2 + 1]
                i = i * 2 + 1
            # Swap left child
            elif self.heap[i * 2] < self.heap[i]:
                self.heap[i * 2], self.heap[i] = self.heap[i], self.heap[i * 2]
                i = i * 2
            else:
                break
        return res
    
    def get_min(self):
        return self.heap[1] if len(self.heap) > 1 else None
    
    def get_len(self):
        return len(self.heap) - 1


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = Heap()

        for num in nums:
            if heap.get_len() == k and num <= heap.get_min():
                continue
            heap.push(num)
            if heap.get_len() > k:
                heap.pop()
        return heap.get_min()

# Time: O(nlogk)
# Space: O(k)
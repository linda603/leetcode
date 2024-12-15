class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        
        def profit(a, b):
            return (a + 1) / (b + 1) - a / b
        
        max_heap = []
        for a, b in classes:
            max_heap.append([-profit(a, b), a, b])
        heapq.heapify(max_heap)

        for i in range(extraStudents):
            p, a, b = heapq.heappop(max_heap)
            heapq.heappush(max_heap, [-profit(a + 1, b + 1), a + 1, b + 1])
        
        return sum(a / b for p, a, b in max_heap) / len(classes)

# Time: O(n + logn + extraStudent*logn). n: len(classes)
# Space: O(n)
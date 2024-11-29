class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for p in points:
            x, y = p
            dist = x * x + y * y
            heapq.heappush(heap, (-dist, p))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        while heap:
            dist, p = heapq.heappop(heap)
            res.append(p)
        return res

# Time: O(nlogk + k) = O(nlogk)
# Space: O(k) 
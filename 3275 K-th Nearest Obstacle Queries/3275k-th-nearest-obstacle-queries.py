class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        heap = []
        res = [-1] * len(queries)

        for i, (x, y) in enumerate(queries):
            heapq.heappush(heap, -(abs(x) + abs(y)))
            # heap = [3]
            if len(heap) > k:
                heapq.heappop(heap)
            if i < k - 1:
                continue
            res[i] = -heap[0]   
        return res

# Time: O(nlogk)
# Space: O(k)
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        max_heap1 = [] # max heap

        for arr, limit in zip(grid, limits):
            max_heap2 = [-num for num in arr]
            heapq.heapify(max_heap2)
            while limit:
                heapq.heappush(max_heap1, heapq.heappop(max_heap2))
                limit -= 1
        
        res = 0
        while k:
            res += -heapq.heappop(max_heap1)
            k -= 1
        return res

# Time: O(nlogn)
# Space: O(n)


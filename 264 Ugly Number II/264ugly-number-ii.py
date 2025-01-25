class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        visited = set()

        while len(visited) < n:
            num = heapq.heappop(heap)
            if num in visited:
                continue
            visited.add(num)
            if len(visited) == n:
                return num
            for prime in [2, 3, 5]:
                val = num * prime
                if val not in visited:
                    heapq.heappush(heap, val)
        
# Time: O(nlogm). m: size of heap
# Space: O(m)
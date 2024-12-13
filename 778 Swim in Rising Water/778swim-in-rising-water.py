class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [[grid[0][0], 0, 0]] # time, r, c
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while heap:
            time, r, c = heapq.heappop(heap)
            if r == n - 1 and c == n - 1:
                return time
            if (r, c) in visited:
                continue
            visited.add((r, c))
            for dr, dc in directions:
                nei_r = r + dr
                nei_c = c + dc
                if nei_r in range(n) and nei_c in range(n) and (nei_r, nei_c) not in visited:
                    new_time = max(time, grid[nei_r][nei_c])
                    heapq.heappush(heap, [new_time, nei_r, nei_c])
        return -1

# Time: O(n^2logn^2) = O(n^2logn)
# Space: O(n^2)
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while heap:
            depth, r, c = heapq.heappop(heap)
            if r == n - 1 and c == n - 1:
                return depth
            for dr, dc in directions:
                nei_r = r + dr
                nei_c = c + dc
                if 0 <= nei_r < n and 0 <= nei_c < n and (nei_r, nei_c) not in visited:
                    heapq.heappush(heap, (max(grid[nei_r][nei_c], depth), nei_r, nei_c))
                    visited.add((nei_r, nei_c))

# Time: O(n^2logn^2)
# Space: O(n^2)
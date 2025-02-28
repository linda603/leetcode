class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        heap = [(0, 0, 0)] # (diff, r, c)
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while heap:
            diff, r, c = heapq.heappop(heap)
            if r == m - 1 and c == n - 1:
                return diff
            if (r, c) in visited:
                continue
            visited.add((r, c))
            for dr, dc in directions:
                nei_r = r + dr
                nei_c = c + dc
                if 0 <= nei_r < m and 0 <= nei_c < n and (nei_r, nei_c) not in visited:
                    new_diff = max(diff, abs(heights[nei_r][nei_c] - heights[r][c]))
                    heapq.heappush(heap, (new_diff, nei_r, nei_c))

# Time: O(mnlogmn)
# Space: O(mn)
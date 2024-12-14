class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if min(grid[0][1], grid[1][0]) > 1:
            return -1

        m, n = len(grid), len(grid[0])
        heap = [[0, 0, 0]] # maxtime, r, c
        visited = set()
        time = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while heap:
            time, r, c = heapq.heappop(heap)
            if r == m - 1 and c == n - 1:
                return time
            if (r, c) in visited:
                continue
            visited.add((r, c))
            for dr, dc in directions:
                nei_r = r + dr
                nei_c = c + dc
                if nei_r in range(m) and nei_c in range(n):
                    wait = 0
                    if abs(grid[nei_r][nei_c] - time) % 2 == 0:
                        wait = 1
                    next_time = max(time + 1, grid[nei_r][nei_c] + wait)
                    heapq.heappush(heap, [next_time, nei_r, nei_c])
        return -1

# Time: O(mnlogmn)
# Space: O(mn)
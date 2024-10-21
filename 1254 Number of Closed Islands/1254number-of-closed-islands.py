class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # dfs/ bfs algorithm to find number of islands and mark it to visited but only add +1 to res if none of positions are on the border
        m, n = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        # return True if none of val 0 at the border
        def bfs(r, c):
            res = True
            queue = collections.deque([(r, c)])
            grid[r][c] = -1

            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nei_r = r + dr
                    nei_c = c + dc
                    if not (0 <= nei_r < m and 0 <= nei_c < n):
                        res = False
                    elif grid[nei_r][nei_c] == 0:
                        queue.append((nei_r, nei_c))
                        grid[nei_r][nei_c] = -1 # Mark all neighbors with value 0 = -1
            return res

        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    if bfs(r, c):
                        print(r, c)
                        res += 1
        return res

# Time: O(mn)
# Space: O(min(m, n))
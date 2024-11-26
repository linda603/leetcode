class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            if r < 0 or r == m or c < 0 or c == n or grid[r][c] != 1:
                return
            grid[r][c] = 2 # mark as visited
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            return

        for r in range(m):
            dfs(r, 0)
            dfs(r, n - 1)
        for c in range(n):
            dfs(0, c)
            dfs(m - 1, c)
        
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    res += 1
        return res

# Time: O(mn)
# Space: O(mn)
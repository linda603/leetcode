class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            for dr, dc in directions:
                nei_r = r + dr
                nei_c = c + dc
                dfs(nei_r, nei_c)
            return
        
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    res += 1
                    dfs(r, c)
        return res

# Time: O(mn)
# Space: O(mn)
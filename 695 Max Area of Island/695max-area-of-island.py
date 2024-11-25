class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def dfs(r, c):
            if r < 0 or r == m or c < 0 or c == n or grid[r][c] != 1 or (r, c) in visited:
                return 0
            area = 1
            visited.add((r, c))
            for dr, dc in directions:
                nei_r = r + dr
                nei_c = c + dc
                area += dfs(nei_r, nei_c)
            return area

        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and (r, c) not in visited:
                    res = max(res, dfs(r, c))
        return res

# Time: O(mn)
# Space: O(mn)
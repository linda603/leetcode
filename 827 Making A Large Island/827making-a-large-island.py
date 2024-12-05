class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        mapping = {} # color island: size
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, color):
            if r < 0 or r == n or c < 0 or c == n or grid[r][c] != 1:
                return 0
            grid[r][c] = color
            res = 1
            for dr, dc in directions:
                nei_r = dr + r
                nei_c = dc + c
                res += dfs(nei_r, nei_c, color)
            return res

        color = 2
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    size = dfs(r, c, color)
                    mapping[color] = size
                    color += 1
        
        res = max(mapping.values()) if mapping else 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    neighbors = set()
                    for dr, dc in directions:
                        nei_r = r + dr
                        nei_c = c + dc
                        if nei_r in range(n) and nei_c in range(n) and grid[nei_r][nei_c] != 0:
                            neighbors.add(grid[nei_r][nei_c])
                    curr_area = 1
                    for color in neighbors:
                        curr_area += mapping[color]
                    res = max(res, curr_area)
        return res

# Time: O(mn + mn*4) = O(mn)
# Space: O(mn). O(mn) for dfs() calls. O(mn) for mapping


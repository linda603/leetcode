class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        cache = {}
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, prev):
            if r < 0 or r == m or c < 0 or c == n or (r, c) in visited or matrix[r][c] <= prev:
                return 0
            if (r, c) in cache:
                return cache[(r, c)]
            cache[(r, c)] = 1
            visited.add((r, c))
            for dr, dc in directions:
                nei_r = r + dr
                nei_c = c + dc
                cache[(r, c)] = max(cache[(r, c)], 1 + dfs(nei_r, nei_c, matrix[r][c]))
            visited.remove((r, c))
            return cache[(r, c)]
        
        res = 0
        for r in range(m):
            for c in range(n):
                res = max(res, dfs(r, c, float("-inf")))
        return res

# Time: O(mn). Each cell will be calculated once.
# Space: O(mn)
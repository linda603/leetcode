class Solution:
    def __init__(self):
        self.cache = {}

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        res = float("inf")

        for c in range(n):
            res = min(res, self.dfs(matrix, 0, c))
        return res
    
    def dfs(self, matrix, r, c):
        m, n = len(matrix), len(matrix[0])
        if r == m - 1:
            return matrix[r][c]
        if (r, c) in self.cache:
            return self.cache[(r, c)]
        self.cache[(r, c)] = float("inf")
        for nei_c in range(c - 1, c + 2):
            if self.is_within_matrix(m, n, r + 1, nei_c):
                self.cache[(r, c)] = min(self.cache[(r, c)], matrix[r][c] + self.dfs(matrix, r + 1, nei_c))
        return self.cache[(r, c)]
    
    def is_within_matrix(self, rows, cols, r, c):
        return r in range(rows) and c in range(cols)

# Time: O(mn)
# Space: O(mn + n). O(n) due to dfs() recursive calls, O(mn) due to cache
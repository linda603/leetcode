class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        cache = {} # (r, c): max_length of square
        m, n = len(matrix), len(matrix[0])
        count = 0

        def dfs(r, c):
            nonlocal count
            if r >= m or c >= n:
                return 0
            if (r, c) in cache:
                return cache[(r, c)]
            cache[(r, c)] = 0
            down = dfs(r + 1, c)
            right = dfs(r, c + 1)
            diag = dfs(r + 1, c + 1)

            if matrix[r][c] == 1:
                cache[(r, c)] = 1 + min(down, right, diag)
                count += cache[(r, c)]
            return cache[(r, c)]
        dfs(0, 0)
        return count

# Time: O(mn)
# Space: O(mn)
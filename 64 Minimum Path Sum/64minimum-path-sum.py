class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [float("inf") for c in range(n + 1)]

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if r == m - 1 and c == n - 1:
                    dp[c] = grid[r][c]
                    continue
                dp[c] = grid[r][c] + min(dp[c], dp[c + 1])
        return dp[0]

# Time: O(mn)
# Space: O(n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * (n + 1)
        dp[n - 1] = 1

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                dp[c] += dp[c + 1]
        return dp[0]

# Time: O(mn)
# Space: O(n)
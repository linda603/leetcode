class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        dp = [[0 for j in range(target + 1)] for i in range(n + 1)]
        dp[n][target] = 1

        for r in range(n - 1, -1, -1):
            for c in range(target - 1, -1, -1):
                for val in range(1, k + 1):
                    if c + val <= target:
                        dp[r][c] += dp[r + 1][c + val]
                        dp[r][c] %= MOD
        return dp[0][0]

# Time: O(n*target*k)
# Space: O(n*target)
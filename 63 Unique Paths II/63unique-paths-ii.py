class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] or obstacleGrid[m - 1][n - 1]:
            return 0
        dp = [0 for c in range(n + 1)]

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if r == m - 1 and c == n - 1:
                    dp[c] = 1
                    continue
                if obstacleGrid[r][c]:
                    dp[c] = 0
                    continue
                dp[c] += dp[c + 1]
        return dp[0]

# Time: O(mn)
# Space: O(n)
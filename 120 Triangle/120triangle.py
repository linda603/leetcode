class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        n = len(triangle[m - 1])
        dp = [0 for c in range(n + 1)]

        for r in range(m - 1, -1, -1):
            row = triangle[r]
            for c in range(len(row)):
                dp[c] = row[c] + min(dp[c], dp[c + 1])
        return dp[0]

# Time: O(mn)
# Space: O(n)
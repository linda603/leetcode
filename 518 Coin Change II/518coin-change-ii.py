class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for a in range(amount + 1)]
        dp[amount] = 1

        for i in range(len(coins) - 1, -1, -1):
            for a in range(amount, -1, -1):
                if a + coins[i] <= amount:
                    dp[a] += dp[a + coins[i]]
        return dp[0]

# Time: O(amount*n)
# Space: O(amount)
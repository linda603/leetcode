class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}

        def dfs(i, is_buying):
            if i >= len(prices):
                return 0
            if (i, is_buying) in cache:
                return cache[(i, is_buying)]
            if is_buying:
                buy = dfs(i + 1, False) - prices[i]
                cool_down = dfs(i + 1, True)
                max_profit = max(buy, cool_down)
            else:
                sell = dfs(i + 2, True) + prices[i]
                cool_down = dfs(i + 1, False)
                max_profit = max(sell, cool_down)
            cache[(i, is_buying)] = max_profit
            return max_profit
        
        return dfs(0, True)

# Time: O(2n)
# Space: O(2n)

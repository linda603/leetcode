class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        
        def dfs(i, is_buying, k):
            if i >= len(prices) or k == 0:
                return 0
            if (i, is_buying, k) in cache:
                return cache[(i, is_buying, k)]
            if is_buying:
                buy = dfs(i + 1, False, k) - prices[i]
                idle = dfs(i + 1, True, k)
                cache[(i, is_buying, k)] = max(buy, idle)
            else:
                sell = dfs(i + 1, True, k - 1) + prices[i]
                idle = dfs(i + 1, False, k)
                cache[(i, is_buying, k)] = max(sell, idle)
            return cache[(i, is_buying, k)]
        return dfs(0, True, 2)

# Time: O(n*2*2) = O(n)
# Space: O(n*2*2) = O(n)
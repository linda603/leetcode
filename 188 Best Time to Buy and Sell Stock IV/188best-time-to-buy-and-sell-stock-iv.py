class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        cache = {}

        def dfs(i, buying, k):
            if i >= len(prices) or k <= 0:
                return 0
            if (i, buying, k) in cache:
                return cache[(i, buying, k)]
            cache[(i, buying, k)] = float("-inf")
            if buying:
                buy = dfs(i + 1, False, k) - prices[i]
                not_buy = dfs(i + 1, True, k)
                cache[(i, buying, k)] = max(buy, not_buy)
            else:
                sell = dfs(i + 1, True, k - 1) + prices[i]
                not_sell = dfs(i + 1, False, k)
                cache[(i, buying, k)] = max(sell, not_sell)
            return cache[(i, buying, k)]
        
        return dfs(0, True, k)

#Time: O(n*2*k) = O(nk)
#Space: O(nk)
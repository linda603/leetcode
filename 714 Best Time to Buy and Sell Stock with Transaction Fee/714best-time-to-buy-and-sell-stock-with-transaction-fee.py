class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cache = {}
        
        def dfs(i, isBuying):
            if i == len(prices):
                return 0
            if (i, isBuying) in cache:
                return cache[(i, isBuying)]
            if isBuying:
                buy = dfs(i + 1, False) - prices[i]
                notBuy = dfs(i + 1, True)
                maxProfit = max(buy, notBuy)
            else:
                sell = dfs(i + 1, True) + prices[i] - fee
                notSell = dfs(i + 1, False)
                maxProfit = max(sell, notSell)
            cache[(i, isBuying)] = maxProfit
            return maxProfit
        
        return dfs(0, True)

#Time: O(2*n)
#Space: O(2*n)
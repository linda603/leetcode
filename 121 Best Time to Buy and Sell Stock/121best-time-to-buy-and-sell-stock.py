class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        best_buy = prices[0]

        for price in prices:
            best_buy = min(best_buy, price)
            res = max(res, price - best_buy)
        return res

# Time: O(n)
# Space: O(1)
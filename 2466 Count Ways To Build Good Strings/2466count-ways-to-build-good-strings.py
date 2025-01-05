class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        module = 10 ** 9 + 7
        res = 0
        cache = {}

        def dfs(i):
            nonlocal res
            if i > high:
                return 0
            if i in cache:
                return cache[i]
            cache[i] = 0
            if low <= i <= high:
                cache[i] += 1
            cache[i] += dfs(i + zero) + dfs(i + one)
            cache[i] %= module
            return cache[i]
        return dfs(0)

# Time: O(2^(high/min(zero, one))) => O(high)
# Space: O(high) due to dfs() depth and caching
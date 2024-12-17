class Solution:
    def minDays(self, n: int) -> int:
        cache = {}

        def dfs(remain):
            if remain <= 1:
                return remain
            if remain in cache:
                return cache[remain]
            cache[remain] = 1 + min(remain % 2 + dfs(remain // 2), remain % 3 + dfs(remain // 3))
            return cache[remain]
        return dfs(n)

# Time: O(max(log(2)n, log(3)n)) = O(log(2)n)
# Space: O(log(2)n)
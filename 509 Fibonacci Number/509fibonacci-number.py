class Solution:
    def fib(self, n: int) -> int:
        cache = {0: 0, 1: 1}
        
        def dfs(n):
            if n in cache:
                return cache[n]
            cache[n] = dfs(n - 1) + dfs(n - 2)
            return cache[n]

        return dfs(n)

# Time: O(2^n) -> O(n)
# Space: O(n)
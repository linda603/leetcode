class Solution:
    def myPow(self, x: float, n: int) -> float:

        def dfs(x, n):
            if x == 0: return 0
            if n == 0: return 1

            res = dfs(x, n // 2)
            res = res * res
            if n % 2: # odd number
                res *= x
            return res

        res = dfs(x, abs(n))
        return res if n >= 0 else 1 / res

# Time: O(logn)
# Space: O(logn)
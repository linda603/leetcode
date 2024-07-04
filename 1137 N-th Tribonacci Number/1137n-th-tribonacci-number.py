class Solution:
    def tribonacci(self, n: int) -> int:
        cache = {0: 0, 1: 1, 2: 1}

        def dfs(i):
            if i in cache:
                return cache[i]
            res = dfs(i - 3) + dfs(i - 2) + dfs(i - 1)
            cache[i] = res
            return res
        return dfs(n)

#Time: O(n) dfs(i) is called once
#Space: O(n). Hash map cache contain n + 1 elements
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def dfs(i, j):
            if j >= len(p):
                return i >= len(s)
            if (i, j) in cache:
                return cache[(i, j)]
            cache[(i, j)] = False
            # case: match = True
            if i < len(s) and (s[i] == p[j] or p[j] == "?"):
                cache[(i, j)] = dfs(i + 1, j + 1)
            elif p[j] == "*":
                # pick j or skip j
                cache[(i, j)] = (i < len(s) and dfs(i + 1, j)) or dfs(i, j + 1)
            return cache[(i, j)]
        return dfs(0, 0)

# Time: O(mn)
# Space: O(mn)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def dfs(i, j):
            if i == 2 and j == 0:
                print("here")
            if j >= len(p):
                return i >= len(s)
            if (i, j) in cache:
                return cache[(i, j)]
            cache[(i, j)] = False
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            print(i, j)
            if j + 1 < len(p) and p[j + 1] == "*":
                # choose * based on previous element or skip *
                cache[(i, j)] = (match and dfs(i + 1, j)) or dfs(i, j + 2)
            elif match:
                cache[(i, j)] = dfs(i + 1, j + 1)
            return cache[(i, j)]
        return dfs(0, 0)

# Time: O(mn)
# Space: O(mn)

# Time: O(mn)
# Space: O(mn)
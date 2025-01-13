class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        res = []
        cache = {}

        def dfs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            if text1[i] == text2[j]:
                cache[(i, j)] = 1 + dfs(i + 1, j + 1)
            else:
                cache[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))
            return cache[(i, j)]
        return dfs(0, 0)

# Time: O(mn)
# Space: O(mn)
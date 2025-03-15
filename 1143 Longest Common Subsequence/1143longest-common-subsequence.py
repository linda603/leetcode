class Solution:
    def __init__(self):
        self.cache = {}

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.dfs(text1, text2, 0, 0)
    
    def dfs(self, text1, text2, i, j):
        if i >= len(text1) or j >= len(text2):
            return 0
        if (i, j) in self.cache:
            return self.cache[(i, j)]
        self.cache[(i, j)] = 0
        if text1[i] == text2[j]:
            self.cache[(i, j)] = 1 + self.dfs(text1, text2, i + 1, j + 1)
        else:
            self.cache[(i, j)] = max(self.dfs(text1, text2, i + 1, j), self.dfs(text1, text2, i, j + 1))
        return self.cache[(i, j)]

# Time: O(mn)
# Space: O(mn)
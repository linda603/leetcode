class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}
        
        def dfs(i, j):
            if i >= len(word1):
                return len(word2) - j
            if j >= len(word2):
                return len(word1) - i
            if (i, j) in cache:
                return cache[(i, j)]
            if word1[i] == word2[j]:
                cache[(i, j)] = dfs(i + 1, j + 1)
            else:
                replace = 1 + dfs(i + 1, j + 1)
                delete = 1 + dfs(i + 1, j)
                insert = 1 + dfs(i, j + 1)
                cache[(i, j)] = min(replace, delete, insert)
            return cache[(i, j)]
        return dfs(0, 0)

# Time: O(3^max(m,n)) -> O(mn)
# Space: O(mn)
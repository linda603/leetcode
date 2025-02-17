class Solution:
    def __init__(self):
        self.cache = {}

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.dfs(s, wordDict, 0)
    
    def dfs(self, s, wordDict, i):
        if i >= len(s):
            return True
        if i in self.cache:
            return self.cache[i]
        self.cache[i] = False
        for word in wordDict:
            if i + len(word) <= len(s) and s[i: i + len(word)] == word and self.dfs(s, wordDict, i + len(word)):
                self.cache[i] = True
                break
        return self.cache[i]

# Time: O(n*m*w) = O(nm)
# Space: O(n + w)
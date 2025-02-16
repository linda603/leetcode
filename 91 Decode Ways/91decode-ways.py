class Solution:
    def __init__(self):
        self.cache = {}

    def numDecodings(self, s: str) -> int:
        return self.dfs(s, 0)
    
    def dfs(self, s, i):
        if i >= len(s):
            return 1
        if s[i] == "0":
            return 0
        if i in self.cache:
            return self.cache[i]
        self.cache[i] = self.dfs(s, i + 1)
        if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
            self.cache[i] += self.dfs(s, i + 2)
        return self.cache[i]
        
# Time: O(2^n) -> O(n)
# Space: O(n)
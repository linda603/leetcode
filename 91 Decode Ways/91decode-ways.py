class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
        
        def dfs(i):
            if i >= len(s):
                return 1
            if i in cache:
                return cache[i]
            if s[i] == "0":
                return 0
            cache[i] = dfs(i + 1)
            if (i + 1 < len(s)) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                cache[i] += dfs(i + 2)
            return cache[i]
        return dfs(0)

# Time: O(n)
# Space: O(n)
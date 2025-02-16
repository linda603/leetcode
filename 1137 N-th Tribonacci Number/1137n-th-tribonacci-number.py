class Solution:
    def __init__(self):
        self.cache = {0: 0, 1: 1, 2: 1}

    def tribonacci(self, n: int) -> int:
        return self.dfs(n)
    
    def dfs(self, i):
        if i in self.cache:
            return self.cache[i]
        self.cache[i] = self.dfs(i - 3) + self.dfs(i - 2) + self.dfs(i - 1)
        return self.cache[i]

# Time: O(n)
# Space: O(n)
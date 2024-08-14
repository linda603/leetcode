from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        cache = {}
        
        def dfs(x, y):
            if x + y == 0:
                return 0
            if x + y == 2:
                return 2
            if (x, y) in cache:
                return cache[(x, y)]
            cache[(x, y)] =  1 + min(dfs(abs(x - 2), abs(y - 1)), dfs(abs(x - 1), abs(y - 2)))
            return cache[(x, y)]
        
        return dfs(abs(x), abs(y))

#Time: O(abs(x*y))
#Space: O(abs(x*y)) depth of dfs is max(abs(x), abs(y)). caching is abs(x*y)
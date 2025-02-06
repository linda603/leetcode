class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        res = 0
        cache = {}

        def dfs(i, prev):
            if i >= len(costs):
                return 0
            if (i, prev) in cache:
                return cache[(i, prev)]
            cache[(i, prev)] = float("inf")
            for color in range(3):
                if color == prev:
                    continue
                cache[(i, prev)] = min(cache[(i, prev)], costs[i][color] + dfs(i + 1, color))
            return cache[(i, prev)]
        
        return dfs(0, -1)
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cache = {}

        def dfs(i):
            if i >= len(days):
                return 0
            if i in cache:
                return cache[i]
            day_pass = costs[0] + dfs(i + 1)
            j = i
            while j < len(days) and days[j] - days[i] + 1 <= 7:
                j += 1
            week_pass = costs[1] + dfs(j)
            j = i
            while j < len(days) and days[j] - days[i] + 1 <= 30:
                j += 1
            month_pass = costs[2] + dfs(j)
            cache[i] = min(day_pass, week_pass, month_pass)
            return cache[i]
        
        return dfs(0)


# Time: O(3^n) -> O((1 + 7 + 30)n)
# Space: O(n)
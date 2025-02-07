class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors = {}
        cnt = {}
        res = [0] * len(queries)

        for i, (ball, color) in enumerate(queries):
            if ball in colors:
                cnt[colors[ball]] -= 1
                if cnt[colors[ball]] == 0:
                    del cnt[colors[ball]]
            colors[ball] = color
            cnt[color] = 1 + cnt.get(color, 0)
            res[i] = len(cnt)
        return res

# Time: O(n). n: len(queries)
# Space: O(limit + n)
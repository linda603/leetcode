class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points_set = set([(x, y) for x, y in points])
        res = float("inf")

        for x1, y1 in points_set:
            for x2, y2 in points_set:
                if x1 < x2 and y1 < y2:
                    if (x1, y2) in points_set and (x2, y1) in points_set:
                        curr_area = (x2 - x1) * (y2 - y1)
                        res = min(res, curr_area)
        return res if res != float("inf") else 0

# Time: O(n + n^2)
# Space: O(n)


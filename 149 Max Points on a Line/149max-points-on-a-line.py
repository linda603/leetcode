class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 1

        for i in range(len(points) - 1):
            count = {}
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                # p1, p2 are in vertical line
                if x1 == x2:
                    slope = float("inf")
                else:
                    slope = (y2 - y1) / (x2 - x1)
                if slope not in count:
                    count[slope] = 1
                count[slope] += 1
                res = max(res, count[slope])
        return res

# Time: O(n^2)
# Space: O(n)
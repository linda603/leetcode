class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        res = len(points)
        points = sorted(points, key = lambda x: x[0])

        # only care about the intersection that overlapping
        prev_end = points[0][1]
        for i in range(1, len(points)):
            start, end = points[i]

            # detect 2 overlapping intervals
            # merge overlapping section by taking the minimum endings
            if start <= prev_end:
                res -= 1
                prev_end = min(prev_end, end)
            else:
                prev_end = end
        
        return res

# Time: O(nlogn + n)
# Space: O(n)

            

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = 0
        l = float("inf")
        r = float("-inf")

        for x, y, length in squares:
            total_area += length * length
            l = min(l, y)
            r = max(r, y + length)
        target = total_area / 2
        res = r

        # Binary search to find min possible mid (horizontal line y)
        for i in range(100):
            mid = (l + r) / 2
            area_below = self.get_area_below(squares, mid)
            if area_below >= target:
                res = mid # need to find minimum line
                r = mid
            elif area_below < target:
                l = mid
        return res

    def get_area_below(self, squares, mid):
        area_below = 0
        for x, y, l in squares:
            # if mid <= y: area_below += 0
            # the whole area is below mid line
            if mid >= y + l:
                area_below += l * l
            # mid line cross the square
            elif mid > y and mid < y + l:
                area_below += (mid - y) * l
        return area_below

# Time: O(nlog(r - l))
# Space: O(1)
                    
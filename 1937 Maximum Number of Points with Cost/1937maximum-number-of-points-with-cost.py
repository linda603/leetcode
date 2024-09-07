class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        if rows == 1: return max(points[0])
        if cols == 1: return sum(sum(x) for x in points)

        def cal_left(row):
            left = [row[0]] + [0] * (cols - 1)
            for c in range(1, cols):
                left[c] = max(row[c], left[c - 1] - 1)
            return left

        def cal_right(row):
            right = [0] * (cols - 1) + [row[cols - 1]]
            for c in range(cols - 2, -1, -1):
                right[c] = max(row[c], right[c + 1] - 1)
            return right
        

        prev = points[0]
        for r in range(1, rows):
            left = cal_left(prev)
            right = cal_right(prev)
            curr = [0] * cols

            for c in range(cols):
                curr[c] = points[r][c] + max(left[c], right[c])
            prev = curr
        
        return max(prev)

#Time: O(n*m*3) = O(n*m). n: rows, n: cols
#Space: O(3*m)
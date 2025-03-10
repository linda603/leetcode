class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l = 0
        r = m * n - 1

        while l <= r:
            mid = (l + r) // 2
            val = matrix[mid // n][mid % n]
            if val == target:
                return True
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1
        return False

# Time: O(log(mn))
# Space: O(1)
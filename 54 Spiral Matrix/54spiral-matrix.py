class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1

        while left <= right and top <= bottom:
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            for r in range(top + 1, bottom + 1):
                res.append(matrix[r][right])
            for c in range(right - 1, left - 1, -1):
                if top == bottom:
                    break
                res.append(matrix[bottom][c])
            for r in range(bottom - 1, top, -1):
                if left == right:
                    break
                res.append(matrix[r][left])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return res

# Time: O(mn)
# Space: O(mn)
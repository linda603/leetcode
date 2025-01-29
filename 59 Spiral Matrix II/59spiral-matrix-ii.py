class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for c in range(n)] for r in range(n)]
        val = 1
        left, right = 0, n - 1
        top, bottom = 0, n - 1

        while left <= right and top <= bottom:
            for c in range(left, right + 1):
                matrix[top][c] = val
                val += 1
            for r in range(top + 1, bottom + 1):
                matrix[r][right] = val
                val += 1
            for c in range(right - 1, left - 1, -1):
                if top == bottom:
                    break
                matrix[bottom][c] = val
                val += 1
            for r in range(bottom - 1, top, -1):
                if left == right:
                    break
                matrix[r][left] = val
                val += 1
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return matrix

# Time: O(n^2)
# Space: O(n^2)
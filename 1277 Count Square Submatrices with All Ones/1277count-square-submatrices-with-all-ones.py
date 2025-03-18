class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        count = 0

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if matrix[r][c] == 1:

                    if r != m - 1 and c != n - 1:
                        matrix[r][c] += min(matrix[r + 1][c], matrix[r][c + 1], matrix[r + 1][c + 1])
                    count += matrix[r][c]
        return count

# Time: O(mn)
# Space: O(1)
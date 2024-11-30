class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        neg = 0
        minVal = float('inf')
        sum_abs = 0

        for row in matrix:
            for val in row:
                if val < 0:
                    neg += 1
                sum_abs += abs(val)
                minVal = min(minVal, abs(val))

        if neg % 2 == 1:
            sum_abs -= 2 * minVal

        return sum_abs
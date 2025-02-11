# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m, n = binaryMatrix.dimensions()
        res = n
        leftmost = n

        for row in range(m):
            l = 0
            r = n - 1

            while l <= r:
                mid = (l + r) // 2
                if binaryMatrix.get(row, mid) == 0:
                    l = mid + 1
                else:
                    leftmost = mid
                    r = mid - 1
            res = min(res, leftmost)
        return res if res != n else -1

# Time: O(m*logn)
# Space: O(1)
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        l = matrix[0][0]
        r = matrix[n - 1][n - 1]

        while l <= r:
            mid = l + (r - l) // 2
            # check how many elements are smaller than mid, if k elements <= mid, this is the right range, reduce r
            count = self.count_smaller(matrix, mid)
            if count >= k:
                r = mid - 1
            else:
                l = mid + 1
        return l

    def count_smaller(self, matrix, target):
        n = len(matrix)
        res = 0

        for row in range(n):
            l = 0
            r = n - 1
            p = n - 1

            if target < matrix[row][l]:
                break
            if target > matrix[row][r]:
                res += n
                continue

            while l <= r:
                mid = l + (r - l) // 2
                if matrix[row][mid] <= target:
                    p = mid
                    l = mid + 1
                else:
                    r = mid - 1
            res += p + 1
        return res

# Time: O(log(max - min)*nlogn) = O(nlogn)
# Space: O(1)
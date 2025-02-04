class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        m = len(nums)
        max_len_c = 0
        diag = defaultdict(list)

        for r in range(m):
            row = nums[r]
            max_len_c = max(max_len_c, len(row))
            for c in range(len(row)):
                diag[r + c].append(nums[r][c])
        
        res = []
        for r in range(m):
            res += diag[r + 0][::-1]
        
        for c in range(1, max_len_c):
            res += diag[m - 1 + c][::-1]

        return res

# Time: O(mn + m*m + n*m) = O(mn)
# Space: O(mn + mn)
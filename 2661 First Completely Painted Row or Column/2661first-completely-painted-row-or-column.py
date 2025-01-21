class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        pos = {}

        for r in range(m):
            for c in range(n):
                pos[mat[r][c]] = (r, c)
        
        count_rows = [0] * m
        count_cols = [0] * n
        for i in range(len(arr)):
            r, c = pos[arr[i]]
            count_rows[r] += 1
            count_cols[c] += 1
            if count_rows[r] == n or count_cols[c] == m:
                return i

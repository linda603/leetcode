class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        pos_diag = set() # r + c
        neg_diag = set() # r - c

        def dfs(r):
            if r == n:
                return 1 # able to make n-queens in n x n board
            res = 0
            for c in range(n):
                if c not in cols and r + c not in pos_diag and r - c not in neg_diag:
                    cols.add(c)
                    pos_diag.add(r + c)
                    neg_diag.add(r - c)
                    res += dfs(r + 1)
                    cols.remove(c)
                    pos_diag.remove(r + c)
                    neg_diag.remove(r - c)

            return res

        return dfs(0)

# Time: O(n!). First row, we have n choices, next row, we have n - 1 choices
# Space: O(n) dfs recursion calls
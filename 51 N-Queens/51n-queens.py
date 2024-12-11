class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        cols = set()
        pos_diag = set()
        neg_diag = set()
        res = []

        def backtrack(r):
            nonlocal res
            if r == n:
                tmp = ["".join(row) for row in board]
                res.append(tmp)
                return
            for c in range(n):
                if c not in cols and (r + c) not in pos_diag and (r - c) not in neg_diag:
                    board[r][c] = "Q"
                    cols.add(c)
                    pos_diag.add(r + c)
                    neg_diag.add(r - c)
                    backtrack(r + 1)

                    board[r][c] = "."
                    cols.remove(c)
                    pos_diag.remove(r + c)
                    neg_diag.remove(r - c)
            return
        
        backtrack(0)
        return res

# Time: O(n! * n^2). n! for backtrack(), n^2 for tmp building
# Space: O(3n + n^2) = O(n^2)
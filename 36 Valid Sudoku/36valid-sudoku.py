class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                val = board[r][c]
                curr_box = (r // 3) * 3 + c // 3
                if val in rows[r] or val in cols[c] or val in boxes[curr_box]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                boxes[curr_box].add(val)
        return True

# Time: O(9^2) = O(1)
# Space: O(3*9^2) = O(1)
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def valid(r, c, char):
            for i in range(9):
                if (board[r][i] == char or board[i][c] == char or 
                    board[(r//3)*3 + i//3][(c//3)*3 + i%3] == char):
                    return False
            return True

        def backtrack(r, c):
            if r == 9: return True
            if c == 9: return backtrack(r + 1, 0)
            if board[r][c] != ".": return backtrack(r, c + 1)

            for num in range(1, 10):
                if valid(r, c, str(num)):
                    board[r][c] = str(num)
                    if backtrack(r, c + 1):
                        return True
                    board[r][c] = "."
            return False
        
        backtrack(0, 0)

# Time: O((9!)^9*9) = O(1). O(9) for is_valid(). Each row we have 9 choices, then next element has 8 choices.
# Space: O(9^2) = O(1)
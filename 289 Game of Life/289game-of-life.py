class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Original | New   | State
        #      0   |  0    |  0
        #      1   |  1    |  1
        #      0   |  1    |  2 
        #      1   |  0    |  3
        #
        rows, cols = len(board), len(board[0])
        
        for r in range(rows):
            for c in range(cols):
                lives = self.calculate_lives(board, r, c)

                if board[r][c] and (lives < 2 or lives > 3):
                    board[r][c] = 3
                elif not board[r][c] and lives == 3:
                    board[r][c] = 2
            
        self.update_board(board)
    
    def calculate_lives(self, board, r, c):
        rows, cols = len(board), len(board[0])
        directions = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]

        lives = 0
        for dr, dc in directions:
            nei_r = r + dr
            nei_c = c + dc
            if nei_r in range(rows) and nei_c in range(cols) and (board[nei_r][nei_c] in [1, 3]):
                lives += 1
        return lives
    
    def update_board(self, board):
        rows, cols = len(board), len(board[0])

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 2:
                    board[r][c] = 1
                elif board[r][c] == 3:
                    board[r][c] = 0

#Time: O(mn*8)
#Space: O(1)
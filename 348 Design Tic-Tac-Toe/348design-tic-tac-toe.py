class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = defaultdict(int)
        self.cols = defaultdict(int)
        self.pos_diag = 0
        self.neg_diag = 0

    def move(self, row: int, col: int, player: int) -> int:
        curr_player = 1 if player == 1 else -1
        self.rows[row] += curr_player
        self.cols[col] += curr_player
        if row == col:
            self.pos_diag += curr_player
        if row == self.n - col - 1:
            self.neg_diag += curr_player
        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(self.pos_diag) == self.n or abs(self.neg_diag) == self.n:
            return player
        return 0

# Time: O(1)
# Space: O(2n)

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
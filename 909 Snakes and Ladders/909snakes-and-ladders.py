class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board.reverse()
        
        def convert_pos(pos):
            r = (pos - 1) // n
            c = (pos - 1) % n
            if r % 2: # if odd row: 1, 3, 5...
                c = n - 1 - c
            return [r, c]

        queue = deque([[1, 0]]) # [pos, moves]
        visited = set()
        visited.add(1)

        while queue:
            pos, moves = queue.popleft()
            if pos == n * n:
                return moves
            for i in range(1, 7):
                next_pos = pos + i
                r, c = convert_pos(next_pos)
                if r in range(n) and c in range(n):
                    if board[r][c] != -1:
                        next_pos = board[r][c]
                    if next_pos not in visited:
                        queue.append([next_pos, moves + 1])
                        visited.add(next_pos)
        return -1

#Time: O(n^2)
#Space: O(n^2)
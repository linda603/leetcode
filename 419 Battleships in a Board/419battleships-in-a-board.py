class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        res = 0
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        if not board:
            return 0
        
        def bfs(r, c):
            queue = collections.deque()
            queue.append((r, c))
            visited.add((r, c))

            while queue:
                r, c = queue.popleft()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if row in range(ROWS) and col in range(COLS) and \
                        (row, col) not in visited and board[row][col] == 'X':
                        queue.append((row, col))
                        visited.add((row, col))

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'X' and (r, c) not in visited:
                    res += 1
                    bfs(r, c)
        return res

#Time: O(m*n)
#Space: O(min(m, n))
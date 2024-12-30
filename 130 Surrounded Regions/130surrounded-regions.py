class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def dfs(r, c):
            if r < 0 or r == m or c < 0 or c == n or board[r][c] != "O":
                return
            board[r][c] = "L"
            for dr, dc in directions:
                nei_r = r + dr
                nei_c = c + dc
                dfs(nei_r, nei_c)
            return  

        for r in range(m):
            dfs(r, 0)
            dfs(r, n - 1)
        for c in range(n):
            dfs(0, c)
            dfs(m - 1, c)
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == "L":
                    board[r][c] = "O"
        
# Time: O(3mn)
# Space: O(mn) max depth of dfs() is O(mn)

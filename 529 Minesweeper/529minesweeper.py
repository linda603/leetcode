class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        directions = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
        
        def dfs(r, c):
            if r < 0 or r == m or c < 0 or c == n or board[r][c] != "E":
                return
            count = 0
            for dr, dc in directions:
                nei_r = r + dr
                nei_c = c + dc
                if nei_r in range(m) and nei_c in range(n) and board[nei_r][nei_c] == "M":
                    count += 1
            if count:
                board[r][c] = str(count)
            else:
                board[r][c] = "B"
                for dr, dc in directions:
                    nei_r = r + dr
                    nei_c = c + dc
                    if nei_r in range(m) and nei_c in range(n) and board[nei_r][nei_c] == "E":
                        dfs(nei_r, nei_c)
                
            return
        
        r, c = click
        if board[r][c] == "M":
            board[r][c] = "X"
        else:
            dfs(r, c)
        return board

# Time: O(mn*8)
# Space: O(mn) depth of dfs
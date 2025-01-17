class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def dfs(i, r, c, visited):
            if i >= len(word):
                return True
            if r < 0 or r == m or c < 0 or c == n or board[r][c] != word[i] or (r, c) in visited:
                return False
            if i == 2:
                print(r, c)
            visited.add((r, c))
            for dr, dc in directions:
                nei_r = r + dr
                nei_c = c + dc
                if dfs(i + 1, nei_r, nei_c, visited):
                    return True
            visited.remove((r, c))
            return False
        
        for r in range(m):
            for c in range(n):
                if dfs(0, r, c, set()):
                    return True
        return False

# Time: O(mn*3^l)
# Space: O(l) depth of dfs()
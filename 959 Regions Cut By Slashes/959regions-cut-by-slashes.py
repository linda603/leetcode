class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        new_len = n * 3
        matrix = [[1 for c in range(new_len)] for r in range(new_len)]

        # scale original to new matrix 3 times size of grid
        for r in range(n):
            for c in range(n):
                new_r = r * 3
                new_c = c * 3
                if grid[r][c] == "/":
                    matrix[new_r][new_c + 2] = 0
                    matrix[new_r + 1][new_c + 1] = 0
                    matrix[new_r + 2][new_c] = 0
                elif grid[r][c] == "\\":
                    matrix[new_r][new_c] = 0
                    matrix[new_r + 1][new_c + 1] = 0
                    matrix[new_r + 2][new_c + 2] = 0
                
        # dfs group region of 1
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r, c):
            if r < 0 or r == new_len or c < 0 or c == new_len or matrix[r][c] == 0:
                return
            matrix[r][c] = 0
            for dr, dc in directions:
                nei_r = r + dr
                nei_c = c + dc
                dfs(nei_r, nei_c)
            return

        res = 0
        for r in range(new_len):
            for c in range(new_len):
                if matrix[r][c] == 1:
                    res += 1
                    dfs(r, c)
        return res

# Time: O(n^2 + 3n*3n) = O(n^2)
# Space: O(n^2 + n^2) = O(n^2)
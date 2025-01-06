class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        matrix = [[0 for c in range(n)] for r in range(m)]
        land = 0

        def bfs(r, c):
            nonlocal land
            min_dist = float("inf")
            queue = collections.deque([(r, c)])
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            level = 1
            while queue:
                for i in range(len(queue)):
                    r, c = queue.popleft()
                    for dr, dc in directions:
                        nei_r = r + dr
                        nei_c = c + dc
                        if nei_r in range(m) and nei_c in range(n) and grid[nei_r][nei_c] == land:
                            grid[nei_r][nei_c] -= 1
                            matrix[nei_r][nei_c] += level
                            min_dist = min(min_dist, matrix[nei_r][nei_c])
                            queue.append((nei_r, nei_c))
                level += 1
            land -= 1
            return min_dist

        res = -1
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    res = bfs(r, c)
        return res if res != float("inf") else - 1

# Time: O(mn*mn)
# Space: O(mn + mn) = O(mn). new matrix takes O(mm), bfs() takes O(mn)
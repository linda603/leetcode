class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1

        queue = deque([(0, 0)])
        visited = set([(0, 0)])

        level = 1
        directions = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == n - 1 and c == n - 1:
                    return level
                for dr, dc in directions:
                    nei_r = dr + r
                    nei_c = dc + c
                    if 0 <= nei_r < n and 0 <= nei_c < n and grid[nei_r][nei_c] == 0 and (nei_r, nei_c) not in visited:
                        visited.add((nei_r, nei_c))
                        queue.append((nei_r, nei_c))
            level += 1
        return -1

# Time: O(n^2)
# Space: O(n^2)
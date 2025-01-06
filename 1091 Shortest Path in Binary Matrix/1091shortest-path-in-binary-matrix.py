class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1
        queue = collections.deque([(0, 0)])
        level = 1
        directions = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]

        visited = set([(0, 0)])
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == n - 1 and c == n - 1:
                    return level
                for dr, dc in directions:
                    nei_r = r + dr
                    nei_c = c + dc
                    if nei_r in range(n) and (nei_c) in range(n) and grid[nei_r][nei_c] == 0 and (nei_r, nei_c) not in visited:
                        queue.append((nei_r, nei_c))
                        visited.add((nei_r, nei_c))
            level += 1
        return -1

# Time: O(mn)
# Space: O(mn)

            
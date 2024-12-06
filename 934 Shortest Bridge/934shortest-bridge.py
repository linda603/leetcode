class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            if r < 0 or r == n or c < 0 or c == n or grid[r][c] == 0 or (r, c) in visited:
                return 
            visited.add((r, c))
            for dr, dc in directions:
                nei_r = r + dr
                nei_c = c + dc
                dfs(nei_r, nei_c)
        
        def bfs():
            queue = collections.deque(visited)
            level = 0

            while queue:
                size = len(queue)
                for i in range(size):
                    r, c = queue.popleft()
                    for dr, dc in directions:
                        nei_r = r + dr
                        nei_c = c + dc
                        if nei_r in range(n) and nei_c in range(n) and (nei_r, nei_c) not in visited:
                            if grid[nei_r][nei_c] == 1:
                                return level
                            queue.append((nei_r, nei_c))
                            visited.add((nei_r, nei_c))

                level += 1

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    # 1. identify the first island
                    dfs(r, c)
                    # 2. bfs layers to check how many 0 to reach 2nd island
                    return bfs()

# Time: O(mn) to do dfs() + bfs()
# Space: O(mn) for dfs() + bfs() + visited set()
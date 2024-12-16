class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r, c):
            if [r, c] == destination:
                return True
            if (r, c) in visited:
                return False
            visited.add((r, c))
            for dr, dc in directions:
                nei_r = r
                nei_c = c
                while nei_r + dr in range(m) and (nei_c + dc) in range(n) and not maze[nei_r + dr][nei_c + dc]:
                    nei_r += dr
                    nei_c += dc
                if dfs(nei_r, nei_c):
                    return True
            return False
            
        return dfs(start[0], start[1])

# Time: O(mn*(m + n)). We visit each pos in maze once. For each pos, loop through the curr row, curr col to stop the ball takes O(m + n)
# Space: O(mn + mn). Depth dfs() O(mn), visited set O(mn)


            
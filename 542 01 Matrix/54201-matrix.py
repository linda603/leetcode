class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        queue = deque()

        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    queue.append((r, c))
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        level = 1
        visited = set()
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nei_r = r + dr
                    nei_c = c + dc
                    if nei_r in range(m) and nei_c in range(n) and mat[nei_r][nei_c] == 1 and (nei_r, nei_c) not in visited:
                        mat[nei_r][nei_c] = level
                        queue.append((nei_r, nei_c))
                        visited.add((nei_r, nei_c))
            level += 1
        return mat

# Time: O(mn + mn)
# Space: O(mn + mn) due to queue + visited set()
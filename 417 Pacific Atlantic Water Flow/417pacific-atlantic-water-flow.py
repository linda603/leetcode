class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific_visited = set()
        atlantic_visited = set()

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r, c , prev, visited):
            if r < 0 or r == rows or c < 0 or c == cols or (r, c) in visited or heights[r][c] < prev:
                return
            visited.add((r, c))
            for dr, dc in directions:
                nei_r, nei_c = r + dr, c + dc
                dfs(nei_r, nei_c, heights[r][c], visited)

        
        for r in range(rows):
            dfs(r, 0, -1, pacific_visited)
            dfs(r, cols - 1, -1, atlantic_visited)
        
        for c in range(cols):
            dfs(0, c, -1, pacific_visited)
            dfs(rows -1, c, -1, atlantic_visited)
        
        res = []
        for r, c in pacific_visited:
            if (r, c) in atlantic_visited:
                res.append([r, c])

        return res

#Time: O(mn)
#Space: O(mn)

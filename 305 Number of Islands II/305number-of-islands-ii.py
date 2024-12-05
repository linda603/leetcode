class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        par = [i for i in range(m*n)]
        visited = set()
        cnt = 0

        def find(x):
            r, c = x
            pos = r * n + c % n
            p = par[pos]
            while p != par[p]:
                p = par[par[p]]
                p = par[p]
        
            return p

        def union(x, y):
            px = find(x)
            py = find(y)

            # cannot union as they have the same parent
            if px == py:
                return False
            par[py] = px
            return True

        res = []
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for r, c in positions:
            if (r, c) not in visited:
                cnt += 1
                visited.add((r, c))
                for dr, dc in directions:
                    nei_r = r + dr
                    nei_c = c + dc
                    if (nei_r, nei_c) in visited:
                        if union((nei_r, nei_c), (r, c)):
                            cnt -= 1
            res.append(cnt)
        return res

# Time: O(mn + p*4). O(mn) to initialize par[]. O(p*4) to loop positions * 4 unions of the neighbors.
# Space: O(mn + p). par[] takes O(mn). res takes O(p)
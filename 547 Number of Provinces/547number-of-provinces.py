class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adj = {i: set() for i in range(n)}

        # to add connected adj to adj {}
        for r in range(n):
            for c in range(n):
                if isConnected[r][c]:
                    adj[r].add(c)
                    adj[c].add(r)

        visited = set()
        def dfs(node):
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)

        res = 0
        for node in range(n):
            if node not in visited:
                res += 1
                dfs(node)
        return res

# Time: O(n*n + n*n). To build adj{} O(n*n)
#       depth dfs() O(n) * interate all possible edges from adj[nei] O(n)
# Space: O(n)
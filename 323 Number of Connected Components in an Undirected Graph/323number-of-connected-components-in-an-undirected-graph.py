class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        visited = set()
        def dfs(node):
            if node in visited:
                return
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

# Time: O(E + V + E)
# Space: O(E + V)
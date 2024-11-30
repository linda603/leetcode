class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        visited = set()
        def dfs(node, prev_node):
            if node in visited:
                return False
            visited.add(node)
            for nei in adj[node]:
                if nei == prev_node:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        if not dfs(0, -1):
            return False
        return True if len(visited) == n else False

# Time: O(E + V + E) = O(V + E)
# Space: O(V + E + V). O(V) for visited set()
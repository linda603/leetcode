class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # Topological sort
        visited = set()
        cycle = set()

        def dfs(node):
            if graph[node] == []:
                if node not in visited:
                    visited.add(node)
                return True
            if node in cycle:
                return False
            cycle.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            cycle.remove(node)
            graph[node] = []
            visited.add(node)
            return True
        
        res = []
        for node in range(len(graph)):
            if dfs(node):
                res.append(node)
        return res

# Time: O(E + V)
# Space: O(V + V)
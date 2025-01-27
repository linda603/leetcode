class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n # 0: even, 1: odd

        def bfs(node):
            if colors[node] != -1:
                return True
            queue = deque([node])
            while queue:
                node = queue.popleft()
                if colors[node] == -1:
                    colors[node] = 0
                for nei in graph[node]:
                    if colors[nei] != -1 and colors[nei] == colors[node]:
                        return False
                    elif colors[nei] == -1:
                        queue.append(nei)
                        colors[nei] = not colors[node]
            return True
        
        for node in range(n):
            if not bfs(node):
                return False
        return True

# Time: O(V(V + E))
# Space: O(V + V)
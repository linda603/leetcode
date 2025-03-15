class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [-1] * len(graph) # 0: even, 1: odd

        for node in range(len(graph)):
            if not self.bfs(graph, colors, node):
                return False
        return True

    def bfs(self, graph, colors, node):
        queue = deque([node])

        while queue:
            node = queue.popleft()
            if colors[node] == -1:
                colors[node] = 0
            for nei in graph[node]:
                if colors[nei] != -1 and colors[nei] == colors[node]:
                    return False
                elif colors[nei] == -1:
                    colors[nei] = not colors[node]
                    queue.append(nei)
        return True

# Time: O(V*(E + V)))
# Space: O(V)
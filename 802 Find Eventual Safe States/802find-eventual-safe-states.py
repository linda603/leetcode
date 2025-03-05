class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        outdegree = [0] * n
        adj = {i: [] for i in range(n)}

        for node in range(n):
            for nei in graph[node]:
                adj[nei].append(node)
            outdegree[node] = len(graph[node])
        
        res = []
        queue = deque()
        # Push all zero indegree nodes in the queue
        for node in range(n):
            if outdegree[node] == 0:
                queue.append(node)
        
        safe_nodes = [0] * n
        while queue:
            node = queue.popleft()
            safe_nodes[node] = 1
            for nei in adj[node]:
                outdegree[nei] -= 1
                if not outdegree[nei]:
                    queue.append(nei)
        
        res = []
        for node in range(n):
            if safe_nodes[node]:
                res.append(node)
        return res

# Time: O(E + V)
# Space: O(E + V)
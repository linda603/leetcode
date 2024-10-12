class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list)
        for i, q in enumerate(equations):
            a, b = q
            adj[a].append([b, values[i]])
            adj[b].append([a, 1 / values[i]])

        def dfs(src, dst):
            queue = collections.deque([(src, 1)]) # [node, weight]
            visited = set([src])

            while queue:
                node, w = queue.popleft()
                if node == dst:
                    return w
                for nei, nei_w in adj[node]:
                    if nei not in visited:
                        queue.append((nei, w * nei_w))
                        visited.add(nei)
            return -1
        
        res = []
        for src, dst in queries:
            if src not in adj or dst not in adj:
                res.append(-1)
            else:
                res.append(dfs(src, dst))
        return res

#Time: O(n*(E + V))
#Space: O(E + V)
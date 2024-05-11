class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        adj = defaultdict(list)

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        #Count edges for every node
        edgeCount = {}
        queue = collections.deque()
        for src, nei in adj.items():
            if len(nei) == 1: #leaf node
                queue.append(src)
            edgeCount[src] = len(nei)
        
        #BFS go though layer by layer
        while queue:
            if n <= 2:
                return list(queue)
            qLen = len(queue)
            for i in range(qLen):
                node = queue.popleft()
                n -= 1
                for nei in adj[node]:
                    edgeCount[nei] -= 1
                    if edgeCount[nei] == 1:
                        queue.append(nei)
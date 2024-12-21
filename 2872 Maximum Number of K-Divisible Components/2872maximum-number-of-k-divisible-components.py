class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if n <= 1 : return 1
        count = 0

        # build adjacency map
        adj = defaultdict(set)
        for u,v in edges: 
            adj[u].add(v)
            adj[v].add(u)
        
        # start with leaves
        queue = collections.deque(u for u, vs in adj.items() if len(vs) == 1)
        
        # cut leaves layer by layer
        while queue:
            for i in range(len(queue)):
                u = queue.popleft()
                
                # get u's parent and remove u from its children
                p = next(iter(adj[u])) if adj[u] else -1
                if p >= 0:
                    adj[p].remove(u)
                
                # either separate a correct component or add to parent
                if values[u] % k == 0 : 
                    count += 1
                else:
                    values[p] += values[u]

                # update queue with new leaves
                if p >= 0 and len(adj[p]) == 1 : queue.append(p)

        return count
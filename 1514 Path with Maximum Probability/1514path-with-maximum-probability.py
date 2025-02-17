class Solution:

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        if start_node == end_node:
            return 1
        adj = self.get_adj(n, edges, succProb)
        heap = [(-1, start_node)]
        visited = set()

        while heap:
            w, node = heapq.heappop(heap)
            if node == end_node:
                return -w
            visited.add(node)
            for nei, nei_w in adj[node]:
                if nei not in visited:
                    heapq.heappush(heap, (w * nei_w, nei))
        return 0



    def get_adj(self, n, edges, succProb):
        adj = {i: [] for i in range(n)}

        for pair, w in zip(edges, succProb):
            a, b = pair
            adj[a].append((b, w))
            adj[b].append((a, w))
        return adj

# Time: O(E + V)
# Space: O(E + V)
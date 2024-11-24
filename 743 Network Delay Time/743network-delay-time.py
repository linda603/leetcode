class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(n + 1)}

        for u, v, w in times:
            adj[u].append([w, v])
        
        heap = [[0, k]] # time, node
        visited = set([k])

        while heap:
            time, node = heapq.heappop(heap)
            if len(visited) == n:
                return time
            visited.add(node)
            for w, nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(heap, [time + w, nei])
        return time if len(visited) == n else -1

# Time: O(E + V + E). E to build adj list. V + E for traversal
# Space: O(V + E) for adj + heap space.

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            adj[u].append((w, v))
        
        heap = [(0, k)] # (time, node)
        visited = set()

        while heap:
            time, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            if len(visited) == n:
                return time
            for nei_w, nei in adj[node]:
                if nei in visited:
                    continue
                heapq.heappush(heap, (time + nei_w, nei))

        return -1

# Time: O(E + V + ElogV)
# Space: O(E + V + V + V)
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {i: [] for i in range(len(points))}

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        
        heap = [(0, 0)] # (dist, node)
        visited = set()

        total = 0
        while heap:
            dist, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            total += dist
            if len(visited) == len(points):
                return total
            for nei_dist, nei in adj[node]:
                if nei in visited:
                    continue
                heapq.heappush(heap, (nei_dist, nei))

# Time: O(n^2 + n^2logn^2). n: len(points). n^2 = E
# Space: O(n^2)
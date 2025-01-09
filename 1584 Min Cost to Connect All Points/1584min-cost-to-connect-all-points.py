class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
        adj = {i: [] for i in range(len(points))}

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                adj[i].append((abs(x1 - x2) + abs(y1 - y2), j))
                adj[j].append((abs(x1 - x2) + abs(y1 - y2), i))
        
        heap = [(0, 0)] # cost, point 0
        total = 0
        visited = set()

        while len(visited) < len(points):
            cost, point = heapq.heappop(heap)
            if point in visited:
                continue
            visited.add(point)
            total += cost
            if len(visited) == len(points):
                return total
            for nei_cost, nei in adj[point]:
                if nei not in visited:
                    heapq.heappush(heap, (nei_cost, nei))
            
# Time: O(V^2 + ElogE) = O(V^2 + ElogV^2) = O(V^2 + ElogV)
# Space: O(E). O(E) due to adj() + O(E) due to heap


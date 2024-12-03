class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        heap = [[0, 0, 0]] # [time, r, c]
        visited = set([])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while heap:
            time, r, c = heapq.heappop(heap)
            if r == m - 1 and c == n - 1:
                return time
            if (r, c) in visited:
                continue
            visited.add((r, c))
            for dr, dc in directions:
                nei_r = r + dr
                nei_c = c + dc
                if nei_r in range(m) and nei_c in range(n) and (nei_r, nei_c) not in visited:
                    heapq.heappush(heap, [max(time, moveTime[nei_r][nei_c]) + 1, nei_r, nei_c])

# Time: O(mnlogmn)
# Space: O(mn + mn). For heap size + visited set() 


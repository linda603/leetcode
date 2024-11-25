class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i: [] for i in range(n)}
        for n1, n2, price in flights:
            adj[n1].append([n2, price])
        
        queue = collections.deque([(src, 0)])
        min_cost = [float("inf")] * n
        level = 0

        while queue and level <= k:
            size = len(queue)
            for i in range(size):
                node, price = queue.popleft()
                for nei, nei_p in adj[node]:
                    if price + nei_p >= min_cost[nei]:
                        continue
                    min_cost[nei] = price + nei_p
                    queue.append((nei, min_cost[nei]))
            level += 1
        return min_cost[dst] if min_cost[dst] != float("inf") else -1

# Time: O(V + E + V + E*K) = O(E*K)
# Space: O(V + E + V). O(V + E) for adj, O(V) for queue
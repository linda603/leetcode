class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        adj = defaultdict(list)

        for bus in range(len(routes)):
            for station in routes[bus]:
                adj[station].append(bus)
        
        bus_visited = set()
        station_visited = set([source])

        level = 0
        queue = collections.deque([source])

        while queue:
            for i in range(len(queue)):
                station = queue.popleft()
                if station == target:
                    return level
                for bus in adj[station]:
                    if bus in bus_visited:
                        continue
                    bus_visited.add(bus)
                    for nei in routes[bus]:
                        if nei in station_visited:
                            continue
                        queue.append(nei)
                        station_visited.add(nei)
            level += 1
        return -1
    
# Time: O(E + V + E + V). E: nl. n: len(routes), l: len(longest route)
# Space: O(E + V)
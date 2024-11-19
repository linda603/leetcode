class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        dislikes_list = defaultdict(list)

        for n1, n2 in dislikes:
            dislikes_list[n1].append(n2)
            dislikes_list[n2].append(n1)
        
        colors = [0] * (n + 1)
        visited = set()
        def bfs(node):
            queue = collections.deque([node])
            visited.add(node)

            while queue:
                size = len(queue)
                for i in range(size):
                    node = queue.popleft()
                    if not colors[node]:
                        colors[node] = 1
                    for nei in dislikes_list[node]:
                        if colors[nei] == colors[node]:
                            return False
                        colors[nei] = -1 * colors[node]
                        if nei not in visited:
                            queue.append(nei)
                            visited.add(nei)
            return True
        
        for node in range(1, n + 1):
            if not colors[node]:
                if not bfs(node):
                    return False
        return True

# Time: O(n*n)
# Space: O(n)
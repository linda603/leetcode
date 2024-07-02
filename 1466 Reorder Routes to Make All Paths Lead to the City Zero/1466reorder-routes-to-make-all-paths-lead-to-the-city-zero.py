class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)} # i: [(nei, sign)] sign = True: from i to nei, False otherwise
        visited = set()
        count = 0 # Number of changes

        for a, b in connections:
            adj[a].append((b, True))
            adj[b].append((a, False))
        
        def dfs(node):
            nonlocal count
            visited.add(node)

            for nei, outgoing in adj[node]:
                if nei not in visited:
                    # Check if nei can reach node. 
                    # If (nei, node) is not in connections, outgoing = true meaning nei can't reach node
                    if outgoing:
                        count += 1
                    dfs(nei)
        
        dfs(0)
        return count

#Time: O(nodes)
#Space: O(nodes)
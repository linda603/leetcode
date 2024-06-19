class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = {i: [] for i in range(n)}

        for parent, child in edges:
            adj[parent].append(child)
            adj[child].append(parent)
        
        def dfs(curr, parent):
            time = 0

            for child in adj[curr]:
                if child == parent:
                    continue
                childTime = dfs(child, curr)

                if childTime or hasApple[child]:
                    time += 2 + childTime
            return time
        
        return dfs(0, -1)

#Time: O(n)
#Space: O(h)
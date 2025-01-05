class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}

        for course, preq in prerequisites:
            adj[course].append(preq)

        visited = set()
        def dfs(node):
            if adj[node] == []:
                return True
            if node in visited:
                return False
            visited.add(node)
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            visited.remove(node)
            adj[node] = []
            return True
        
        for node in range(numCourses):
            if not dfs(node):
                return False
        return True

# Time: O(V + E + V + E) = O(V + E)
# Space: O(V + E + V)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}

        for course, preq in prerequisites:
            adj[course].append(preq)
        
        for i in range(numCourses):
            if not self.dfs(adj, i, set()):
                return False
        return True
    
    def dfs(self, adj, course, visited):
        if adj[course] == []:
            return True
        if course in visited:
            return False
        visited.add(course)
        for nei in adj[course]:
            if not self.dfs(adj, nei, visited):
                return False
        adj[course] = []
        visited.remove(course)
        return True

# Time: O(E + V + E + V)
# Space: O(E + V)
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}
        res = []

        for course, preq in prerequisites:
            adj[course].append(preq)
        
        visited = set()
        cycle = set()

        def dfs(course):
            if adj[course] == []:
                if course not in visited:
                    res.append(course)
                    visited.add(course)
                return True
            if course in cycle:
                return False
            cycle.add(course)
            for nei in adj[course]:
                if not dfs(nei):
                    return False
            cycle.remove(course)
            res.append(course)
            visited.add(course)
            adj[course] = []
            return True

        for course in range(numCourses):
            # detect a cycle, cannot finish the course
            if not dfs(course):
                return []
        return res

# Time: O(E + V + E + V)
# Space: O(E + V + V + V). adj map: O(E + V), visited set O(n)
        
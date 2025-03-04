class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, preq in prerequisites:
            adj[course].append(preq)
            indegree[preq] += 1
        
        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        res = []

        while queue:
            course = queue.popleft()
            res.append(course)
            for nei in adj[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        return res[::-1] if len(res) == numCourses else []

# Time: O(E + V + E + V + V)
# Space: O(E + V)
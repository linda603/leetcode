class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj = {i: [] for i in range(1, n + 1)}

        for course, preq in relations:
            adj[course].append(preq)
    
        visited = {} # course: max_length
        def dfs(course):
            if course in visited:
                return visited[course]
            else:
                visited[course] = -1

            max_length = 1 # max_length
            for preq in adj[course]:
                length = dfs(preq)
                if length == -1: # detect a cycle
                    return -1
                max_length = max(max_length, length + 1)
            visited[course] = max_length
            return max_length
                
        res = 1
        for c in range(1, n + 1):
            length = dfs(c)
            print(c, length)
            if length == -1:
                return -1
            res = max(res, length)

        return res

# Time: O(V + E + V + E)
# Space: O(V + E)
            
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = {i: [] for i in range(-1, n)} #Manager -> [list of employee]

        for i in range(n):
            adj[manager[i]].append(i)

        queue = deque([(headID, 0)]) #Id, time
        res = 0

        while queue:
            id, time = queue.popleft()
            res = max(res, time)

            for employee in adj[id]:
                queue.append((employee, time + informTime[id]))
        return res
        
#Time: O(n)
#Space: O(n)
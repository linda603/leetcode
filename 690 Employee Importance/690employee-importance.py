"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mapping = {} # employee id : all values of this id

        for employee in employees:
            mapping[employee.id] = employee

        def dfs(e_id):
            res = mapping[e_id].importance
            for sub in mapping[e_id].subordinates:
                res += dfs(sub)
            return res
        
        return dfs(id)
        


# Time: O(n + n)
# Space: O(n). O(n) for mapping e_id, O(h) for dfs() calls

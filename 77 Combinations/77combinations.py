class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(i, curr):
            if len(curr) == k:
                res.append(curr.copy())
                return
            for num in range(i, n + 1):
                curr.append(num)
                dfs(num + 1, curr)
                curr.pop()
            return
        
        dfs(1, [])
        return res

#Time: O(n^k*k)
#Space: O(k)
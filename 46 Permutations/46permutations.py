class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    dfs(curr)
                    curr.pop()
            return
        
        dfs([])
        return res

#Time: O(n!*n)
#Space: O(n)
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def dfs(i, curr):
            if len(curr) > 1:
                res.add(tuple(curr))
            if i >= len(nums):
                return
            if not curr or curr[-1] <= nums[i]:
                curr.append(nums[i])
                dfs(i + 1, curr)
                curr.pop()
            dfs(i + 1, curr)
            return
        
        dfs(0, [])
        return res
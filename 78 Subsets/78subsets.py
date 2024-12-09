class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(i, curr):
            nonlocal res
            if i >= len(nums):
                res.append(curr.copy())
                return
            curr.append(nums[i])
            dfs(i + 1, curr)
            curr.pop()
            dfs(i + 1, curr)
        
        dfs(0, [])
        return res

# Time: O(2^n)
# Space: O(n)
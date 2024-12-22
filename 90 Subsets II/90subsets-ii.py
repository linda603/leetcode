class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(i, curr):
            nonlocal res
            if i >= len(nums):
                res.append(curr.copy())
                return
            curr.append(nums[i])
            dfs(i + 1, curr)
            curr.pop()
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            dfs(i + 1, curr)
        dfs(0, [])
        return res

# Time: O(nlogn + n*2^n). 2^n due to dfs() traversing + n curr.copy()
# Space: O(n)

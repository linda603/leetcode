class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        cache = {}
        
        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in cache:
                return cache[(l, r)]
            cache[(l, r)] = 0
            for i in range(l, r + 1):
                cache[(l, r)] = max(cache[(l, r)], dfs(l, i - 1) + nums[l - 1] * nums[i] * nums[r + 1] + dfs(i + 1, r))
            return cache[(l, r)]
        return dfs(1, len(nums) - 2)

# Time: O(n^2*n). There are n^2 subarrays. For each array, there is O(n) loop from l to r
# Space: O(n^2 + n + n). cache: O(n^2), dfs(): O(n). [1] + nums + [1]: O(n)
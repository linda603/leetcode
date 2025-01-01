class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # sum1 - sum2 = target
        # total - sum2 - sum2 = target => sum2 = (total - target) // 2
        # Find how many ways can sum up to sum2

        total = sum(nums)
        if total - target < 0 or (total - target) % 2:
            return 0
        new_target = (total - target) // 2

        dp = [[0 for j in range(new_target + 1)] for i in range(len(nums) + 1)]
        dp[len(nums)][new_target] = 1

        for i in range(len(nums) - 1, -1, -1):
            for j in range(new_target, -1, -1):
                dp[i][j] = dp[i + 1][j]
                if j + nums[i] <= new_target:
                    dp[i][j] += dp[i + 1][j + nums[i]] 

        return dp[0][0]

# Time: O(n*sum(nums))
# Space: O(n*sum(nums))
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        dp = [[False for c in range(target + 1)] for r in range(len(nums) + 1)]

        for i in range(len(nums) + 1):
            dp[i][target] = True

        for i in range(len(nums) - 1, -1, -1):
            for val in range(target - 1, -1, -1):
                if nums[i] == target:
                    return True
                # skip i
                dp[i][val] = dp[i + 1][val]
                if dp[i][val]:
                    continue
                # include i
                if val + nums[i] <= target:
                    dp[i][val] = dp[i + 1][val + nums[i]]
        return dp[0][0]

# Time: O(n*half)
# Space: O(n*half)
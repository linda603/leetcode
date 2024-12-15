class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = 0

        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i, len(nums)):
                curr_sum += nums[j]
                if curr_sum == goal:
                    res += 1
                elif curr_sum > goal:
                    break
        return res

# Time: O(n^2)
# Space: O(1)
class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        res = 0

        for i in range(len(nums)):
            if (i - k < 0 or nums[i] > nums[i - k]) and (i + k >= len(nums) or nums[i] > nums[i + k]):
                res += nums[i]
        return res

# Time: O(n)
# Space: O(1)
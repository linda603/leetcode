class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower, upper]]

        nums.append(upper + 1)
        res = []
        if lower < nums[0]:
            res.append([lower, nums[0] - 1])

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                res.append([nums[i - 1] + 1, nums[i] - 1])
        return res

# Time: O(n)
# Space: O(n) due to res
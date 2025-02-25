class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # all intergers we need to check are from range [1, len(nums) + 1]
        nums_set = set(nums)

        for val in range(1, len(nums) + 2):
            if val not in nums_set:
                return val

# Time: O(n)
# Space: O(n)
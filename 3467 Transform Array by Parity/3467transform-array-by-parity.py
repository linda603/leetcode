class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        count_even = 0

        for num in nums:
            if not num % 2:
                count_even += 1

        for i in range(len(nums)):
            if count_even:
                nums[i] = 0
                count_even -= 1
            else:
                nums[i] = 1
        return nums

# Time: O(n)
# Space: O(1)
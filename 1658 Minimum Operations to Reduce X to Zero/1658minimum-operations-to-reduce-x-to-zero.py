class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        window = -1

        total = 0
        l = 0
        for r in range(len(nums)):
            total += nums[r]
            while l <= r and total > target: #In case target < 0 (x > sum(nums)) that would lead us to out of bound
                total -= nums[l]
                l += 1
            if total == target:
                window = max(window, r - l + 1)
        return len(nums) - window if window != -1 else -1

#Time: O(n)
#Space: O(1)
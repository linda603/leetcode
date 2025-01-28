class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] # monotonic decreasing stack, pair of [num, min_val]
        min_val = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            while stack and stack[-1][0] <= num:
                stack.pop()
            if stack and stack[-1][0] > num and stack[-1][1] < num:
                return True
            stack.append([num, min_val])
            min_val = min(min_val, num)
        return False

# Time: O(2n)
# Space: O(n)
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        attempts = len(nums) - k # number of time can pop from stack if num < stack[-1] to make it lexicographical smaller

        for num in nums:
            while stack and attempts and stack[-1] > num:
                stack.pop()
                attempts -= 1
            stack.append(num)
        
        stack = stack[: len(stack) - attempts]
        return stack

# Time: O(n)
# Space: O(n)
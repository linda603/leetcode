class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort()

        for i in range(len(pairs) - 1, -1, -1):
            curr_time = (target - pairs[i][0]) / pairs[i][1]
            if not stack or (stack and curr_time > stack[-1]):
                stack.append(curr_time)
        return len(stack)

# Time: O(2n)
# Space: O(n)
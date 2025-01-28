class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = [] # monotonic decreasing stack

        for i, num in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < num:
                prev_idx = stack.pop()
                res[prev_idx] = i - prev_idx
            stack.append(i)
        return res

# Time: O(n)
# Space: O(n)
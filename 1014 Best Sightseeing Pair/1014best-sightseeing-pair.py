class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        prefix_max = values[0] - 1
        res = 0

        for i in range(1, len(values)):
            res = max(res, prefix_max + values[i])
            prefix_max = max(prefix_max - 1, values[i] - 1)
        return res

# Time: O(n)
# Space: O(1)
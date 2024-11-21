class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        one = cost[n - 1]
        two = 0

        for i in range(n - 2, -1, -1):
            tmp = one
            one = cost[i] + min(one, two)
            two = tmp
        return min(one, two)

# Time: O(n)
# Space: O(1)
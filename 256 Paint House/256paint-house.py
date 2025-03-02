class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        prev_cost = costs[len(costs) - 1]

        for i in range(len(costs) - 2, -1, -1): # i is the house      
            cost_house_0 = costs[i][0] + min(prev_cost[1], prev_cost[2])
            cost_house_1 = costs[i][1] + min(prev_cost[0], prev_cost[2])
            cost_house_2 = costs[i][2] + min(prev_cost[0], prev_cost[1])

            prev_cost = [cost_house_0, cost_house_1, cost_house_2]
        return min(prev_cost)

# Time: O(n)
# Space: O(1)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        # greedy approach
        total = 0
        start = 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                start = i + 1
                total = 0
        return start if start != len(gas) else - 1

# Time: O(n)
# Space: O(1)
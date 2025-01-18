class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        
        cost_without_arrangement = 0
        for a, b in zip(arr, brr):
            cost_without_arrangement += abs(a - b)

        arr.sort()
        brr.sort()
        cost_with_arrangement = k
        for a, b in zip(arr, brr):
            cost_with_arrangement += abs(a - b)
        return min(cost_without_arrangement, cost_with_arrangement)

# Time: O(n + nlogn + n) = O(nlogn)
# Space: O(n)
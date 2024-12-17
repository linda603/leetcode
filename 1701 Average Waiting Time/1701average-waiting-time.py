class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total = 0
        prev_end = 0
        
        for arrival, time in customers:
            if arrival < prev_end:
                total += prev_end - arrival
            total += time
            prev_end = max(prev_end, arrival) + time
        return total / (len(customers))

# Time: O(n)
# Space: O(1)
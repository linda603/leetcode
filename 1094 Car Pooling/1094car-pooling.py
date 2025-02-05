class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        line_sweep = [0] * 1001

        for passengers, src, dest in trips:
            line_sweep[src] += passengers
            line_sweep[dest] += -passengers
            
        curr_cap = 0
        for station, passengers in enumerate(line_sweep):
            curr_cap += passengers
            if curr_cap > capacity:
                return False
        return True

# Time: O(n + 1001) = O(n)
# Space: O(1001) = O(1)
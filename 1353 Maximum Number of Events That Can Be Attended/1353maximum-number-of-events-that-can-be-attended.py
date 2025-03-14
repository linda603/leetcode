class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()

        total_days = 0
        for start, end in events:
            total_days = max(total_days, end)
        
        i = 0
        heap = []
        res = 0
        for day in range(1, total_days + 1):
            while i < len(events) and events[i][0] == day:
                heapq.heappush(heap, events[i][1])
                i += 1
            # invalid event to attend
            while heap and heap[0] < day:
                heapq.heappop(heap)
            
            # valid event that can attend at curr day
            if heap:
                heapq.heappop(heap)
                res += 1
        return res

# Time: O(nlogn + total_days*logn)
# Space: O(n)
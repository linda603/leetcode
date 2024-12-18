class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = [] # earliest avail time of meeting rooms

        for start, end in intervals:
            if heap and heap[0] <= start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
        return len(heap)

# Time: O(nlogn + n) = O(nlogn)
# space: O(n + n) = O(n)


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        heap = [] # (size of interval, ending point)

        mapping = {}
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                start, end = intervals[i]
                heapq.heappush(heap, (end - start + 1, end))
                i += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            mapping[q] = heap[0][0] if heap else -1
        
        return [mapping[q] for q in queries]

# Time: O(nlogn + qlogq + n + q). n: len(intervals), q: len(queries)
# Space: O(n + q)

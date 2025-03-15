class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        prev_end = None

        for start, end in intervals:
            if prev_end and start < prev_end:
                return False
            prev_end = end
        return True

# Time: O(nlogn)
# Space: O(n)
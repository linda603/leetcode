class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time = [self.convert_to_mins(t) for t in timePoints]
        time.sort()

        min_diff = time[0] + 24 * 60 - time[len(time) - 1]
        for i in range(1, len(time)):
            curr_diff = time[i] - time[i - 1]
            min_diff = min(min_diff, curr_diff)
        return min_diff 
        
    def convert_to_mins(self, string):
        time = string.split(":")
        return int(time[0]) * 60 + int(time[1])

# Time: O(n + nlogn + n) = O(nlogn)
# Space: O(n)
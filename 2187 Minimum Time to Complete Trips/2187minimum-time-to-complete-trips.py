class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        l = min(time)
        r = max(time) * totalTrips
        res = r

        while l <= r:
            mid = (l + r) // 2
            if self.is_valid(time, totalTrips, mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
    
    def is_valid(self, time, totalTrips, required_time):
        cnt = 0

        for t in time:
            cnt += required_time // t
        return cnt >= totalTrips

# Time: O(log(sum(time)))
# Space: O(1)
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        count = [[0, 0]] * n # available time, count
        #heap = []

        for start, end in meetings:
            min_available_time = float("inf")
            delay = True
            for i in range(n):
                avail_time, cnt = count[i]
                if avail_time < min_available_time:
                    min_available_time = avail_time
                    assigned_idx = i
                if start >= avail_time:
                    count[i] = [end, cnt + 1]
                    delay = False
                    break
            if delay:
                diff = min_available_time - start
                count[assigned_idx] = [end + diff, count[assigned_idx][1] + 1]
        #print(count)
        res = 0
        max_cnt = 0
        for i in range(n):
            if count[i][1] > max_cnt:
                max_cnt = count[i][1] 
                res = i
        return res

# Time: O(mlogm + mn)
# Space: O(m + n)
                
                



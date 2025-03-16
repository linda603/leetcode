class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x:x[0])
        avail_rooms = [i for i in range(n)] # min heap of available time
        used_rooms = [] # min heap of ending time
        count = [0] * n
        res = n
        max_count = 0

        for start, end in meetings:
            while used_rooms and used_rooms[0][0] <= start:
                heapq.heappush(avail_rooms, heapq.heappop(used_rooms)[1])

            if avail_rooms:
                room = heapq.heappop(avail_rooms)
                count[room] += 1
                heapq.heappush(used_rooms, (end, room))
            else:
                prev_end, room = heapq.heappop(used_rooms)
                count[room] += 1
                heapq.heappush(used_rooms, (end + prev_end - start, room))
            if count[room] > max_count:
                max_count = count[room]
                res = room
            elif count[room] == max_count:
                res = min(res, room)
        return res

# Time: O(mlogm + mlogn)
# Space: O(m + n)
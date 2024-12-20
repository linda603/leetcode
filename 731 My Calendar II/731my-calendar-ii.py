class MyCalendarTwo:

    def __init__(self):
        self.events = defaultdict(int)

    def book(self, startTime: int, endTime: int) -> bool:
        # increase count of start time +1
        self.events[startTime] += 1
        # decrease count of end time of -1
        self.events[endTime] -= 1

        # active bookings
        count = 0

        # Sweep through the events in order
        for time in sorted(self.events.keys()):
            count += self.events[time]
            
            # tripple booking happens
            if count > 2:
                # reverse the change as this booking is not valid
                self.events[startTime] -= 1
                self.events[endTime] += 1
                if self.events[startTime] == 0:
                    del self.events[startTime]
                if self.events[endTime] == 0:
                    del self.events[endTime]
                return False
        # booking is successful
        return True

# Time: O(nlogn)
# Space: O(n)


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)
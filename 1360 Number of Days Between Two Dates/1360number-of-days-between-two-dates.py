class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        y1, m1, d1 = map(int, date1.split('-'))
        y2, m2, d2 = map(int, date2.split('-'))
        print(self.days_since_1971(y1, m1, d1))
        print(self.days_since_1971(y2, m2, d2))

        return abs(self.days_since_1971(y1, m1, d1) - self.days_since_1971(y2, m2, d2))

    def days_since_1971(self, y, m, d):

        def is_leap(year):
            return year % 4 == 0 and (year % 100 != 0 or year % 1000 == 0)
        
        days = 0
        for i in range(1971, y):
            days += 366 if is_leap(i) else 365
                          #. 1.  2.   3  4.  5.   6.  7.  8  9. 10.  11. 12
        days_per_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if is_leap(y):
            days_per_month[2] = 29
        for i in range(1, m):
            days += days_per_month[i]
        days += (d - 1)
        
        return days

# Time: O(1)
# Space: O(1)
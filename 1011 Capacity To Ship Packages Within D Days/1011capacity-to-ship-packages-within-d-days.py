class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        # choose cap for each ship. If able to ship with cap/belt within days, return cap
        l = max(weights)
        r = sum(weights)
        res = r

        while l <= r:
            mid = (l + r) // 2
            if self.is_valid(weights, days, mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

    # check is able to ship
    def is_valid(self, weights, days, cap):
        count = 1
        remain = cap

        for w in weights:
            if remain - w < 0:
                count += 1
                remain = cap
            remain -= w
        return count <= days
    
# Time: O(log(sum(weights)))
# Space: O(1)

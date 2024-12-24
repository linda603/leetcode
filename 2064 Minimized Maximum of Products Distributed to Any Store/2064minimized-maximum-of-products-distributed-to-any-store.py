class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l = 1
        r = max(quantities)
        res = r

        while l <= r:
            mid = (l + r) // 2
            if self.able_to_distribute(n, quantities, mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
    
    def able_to_distribute(self, n, quantities, items):
        cnt = 0

        for q in quantities:
            cnt += math.ceil(q / items)
        return cnt <= n

# Time: O(log(max(quantities)))
# Space: O(1)
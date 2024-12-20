class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        count = 1
        curr = 1

        while count < k:
            steps = self.cal_steps(n, curr)
            if count + steps <= k:
                curr += 1
                count += steps
            else:
                curr = curr * 10
                count += 1
        return curr
    
    def cal_steps(self, n, val):
        steps = 0
        nei = val + 1

        while val <= n:
            steps += min(nei, n + 1) - val
            val *= 10
            nei *= 10
        return steps

# Time: O((logn)^2)
# Space: O(1)
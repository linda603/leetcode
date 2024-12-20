class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 0

        for i in range(n - 1, -1, -1):
            tmp = one
            one = one + two
            two = tmp
        return one

# Time: O(n)
# Space: O(1)
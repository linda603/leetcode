class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = 0
        prev = 0

        for num in target:
            if num > prev:
                res += num - prev
            prev = num
        return res

# Time: O(n)
# Space: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Brute force
        res = float("inf")
        
        for num in nums:
            res = min(res, num)
        return res

# Time: O(n)
# Space: O(1)

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        count = {}

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                count[product] = 1 + count.get(product, 0)
        
        res = 0
        for product, cnt in count.items():
            # valid tuple
            # number of ways to pick 2 pairs out of n options:
            # NC2 = n! / (n - 2)! * 2! = n * (n - 1) / 2
            if cnt >= 2:
                res += cnt * (cnt - 1) // 2

        return res * 8

# Time: O(n^2 + n^2) = O(n^2)
# Space: O(n^2)
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n + 1)]
        fact = 1

        for i in range(1, n):
            fact *= i

        
        res = ""
        k = k - 1

        while True:
            idx = k // fact
            res += str(nums[idx])
            nums.remove(nums[idx])
            if not nums:
                break
            k = k % fact
            fact = fact // len(nums)
        return res

# Time: O(n * n). While takes O(n) to fill up res. Taking out 1 element nums[idx] takes O(n)
# Space: O(n)
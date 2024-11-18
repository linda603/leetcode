class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums[:]

    def shuffle(self) -> List[int]:
        res = self.nums[:]
        n = len(res)

        for i in range(n):
            j = int(random.random() * n)
            res[i], res[j] = res[j], res[i]
        return res
        
# Time: O(1)
# Space: O(n)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
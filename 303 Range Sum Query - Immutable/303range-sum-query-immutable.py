class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        sum = 0

        for num in nums:
            sum += num
            self.prefix.append(sum)        

    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.prefix[right]
        leftSum = 0
        if left > 0:
            leftSum = self.prefix[left - 1]
        return rightSum - leftSum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

#Time: O(n)
#Space: O(n)
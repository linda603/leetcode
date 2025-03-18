class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sequence = []

        for num in nums:
            if not sequence or sequence[-1] < num:
                sequence.append(num)
            else:
                replace_idx = self.binary_search(sequence, num)
                sequence[replace_idx] = num
        return len(sequence)

    def binary_search(self, sequence, target):
        l = 0
        r = len(sequence) - 1
        res = r

        while l <= r:
            mid = (l + r) // 2
            if sequence[mid] == target:
                return mid
            if sequence[mid] > target:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

# Time: O(nlogn)
# Space: O(n)
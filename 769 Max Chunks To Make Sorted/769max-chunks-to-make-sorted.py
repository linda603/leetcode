class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        count = 0
        diff = 0

        for i, num in enumerate(arr):
            diff += num - i
            count += (diff == 0)
        return count

# Time: O(n)
# Space: O(1)